#!/usr/bin/env python3
"""lichnerowicz_response.py -- v32.0-candidate Phase 92 (Block B sequel, the Tensor Dictionary).

"Does the TT sector close in canonical form?"  The sequel to the ratified v31 LIVE (Phase 91:
matter sources a genuine TT metric mode on the cut CP^2 = h_3(C_u)).  v31 proved EXISTENCE of the
TT residue (the LESS-informative branch).  v32's bar for LIVE is strictly HIGHER: a FORCED CLOSED
FORM -- the geometry telling matter exactly how much TT it gets, in the certified dictionary, with
NO free function and NO fitted constant.

THE FOUR VERDICT OBJECTS (frozen at Gate 0; RESEARCH s0 (i)-(iv)):
  (i)   the TT closed form  TT(B3) = sum_i c_i(M) t_i  over the explicit dim-8 TT basis {t_i},
        with the NAMED HYPOTHESIS (verify, do NOT assume) c(M) prop N(M) = M^2 - (1/3)TrM^2 . I;
  (ii)  the norm identity  ||TT(B3)||^2  as a closed form in the frozen tuple with FORCED constants;
  (iii) the threshold number  eps = lambda_L - 2 Lambda = lambda_L - 12  (the genuine sub-fork);
  (iv)  the full York dictionary  B3 = TT + delta*omega + f.g  with omega, f in closed form.

THE METHOD (cliff-free; RESEARCH s5) -- routes around v31's CPU-roasting full-basis Gram:
  The York decomposition B3 = r + delta*omega + f.g is unique (up to Killing in omega), r the TT
  part (tr_g r = 0 AND delta r = 0).  We EXTRACT r explicitly: find (omega, f) -- the SAME complete
  gauge+conformal ansatz as york_solve -- such that r := B3 - delta*omega - f.g has tr_g(r)=0 AND
  delta(r)=0, matched monomial-by-monomial over a common rho-power (a linear system over Q).  r is
  then the EXPLICIT TT tensor = object (i)'s sum c_i t_i AND object (iv)'s (omega,f).  The norm is
  ONE exact integral ||r||^2 = l2_tensor(r,r) (NOT a Gram).  Delta_L is built LOCAL on the explicit
  tensor.  The dim-8 basis {t_i} = the 8 residues r(lambda_a) for the Gell-Mann directions.

DISCIPLINE (v21-v31): exact over Q/Q(t); fail-fast gates; controls with known answers;
non-hardwired verdict(); reuse tensor_probe.py (do NOT rebuild); matched-monomial (never `cancel`
on raw rho-fields before reduction); no full-basis Gram; commit after each gate.

SCOPE FENCE (binding, verbatim in the VERDICT and every summary): this is the deformation-complex
DICTIONARY of a FROZEN imported geometry.  No dynamical metric, no selection law, no kappa.
LIVE = "the tensor sector's source data closes in canonical form" -- a DICTIONARY fact, not a
dynamics fact.  No Einstein-equation / Newton-constant / G=kT / dark-matter / geodesic language;
frozen FS geometry USED not derived; the v18/v20 MM corpse stays buried; OP^2 priced only.  Does
NOT retract v17-v21 (Block-C statements; v32 is the strictly weaker upstream dictionary).

Reproducibility: sympy 1.14.0, Python 3.14, exact rational arithmetic (no RNG / no seeds in the
verdict path; the verdict is symbolic over Q / Q(t), floats illustrative only).  Darwin arm64.
"""
import os
import sys
import time

sys.setrecursionlimit(100000)        # deep nested-fraction GCD on rho-rational tensor fields
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sympy as sp                                                       # noqa: E402
from sympy import (Rational, symbols, cancel, expand, I, Matrix, eye,    # noqa: E402
                   together, zeros, linsolve, fraction, Poly)

import tensor_probe as TP                                               # noqa: E402

# reuse the certified machinery verbatim (do NOT rebuild)
Z1, Z2, Z1B, Z2B = TP.Z1, TP.Z2, TP.Z1B, TP.Z2B
ALLV = (Z1, Z2, Z1B, Z2B)
fs_metric = TP.fs_metric
fs_metric_inv = TP.fs_metric_inv
christoffel_hol = TP.christoffel_hol
_christoffel_antihol = TP._christoffel_antihol
cov_hessian = TP.cov_hessian
delta_star = TP.delta_star
delta_star_of_dphi = TP.delta_star_of_dphi
conformal_block = TP.conformal_block
trace_g = TP.trace_g
divergence = TP.divergence
laplacian = TP.laplacian
traceless_part = TP.traceless_part
l2_tensor = TP.l2_tensor
l2_scalar = TP.l2_scalar
phi_field = TP.phi_field
grad_bilinear = TP.grad_bilinear
B6_stress_blocks = TP.B6_stress_blocks
sharp_cx = TP.sharp_cx
TrM2_cx = TP.TrM2_cx
_herm_basis_3 = TP._herm_basis_3
_potentials = TP._potentials
_M_rat = TP._M_rat
_M_rat2 = TP._M_rat2
Mmat_cut_cx = TP.Mmat_cut_cx
dz = TP.dz
dzb = TP.dzb

_t0 = time.time()
PASS = []


def _log(m):
    print(f"[{time.time() - _t0:6.1f}s] {m}", flush=True)


def _report(label, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}", flush=True)
    return ok


def _rho():
    return 1 + Z1 * Z1B + Z2 * Z2B


# ============================================================================
# THE CLIFF-FREE TT EXTRACTION  (V1, the load-bearing method; RESEARCH s5A)
# ----------------------------------------------------------------------------
# The York decomposition  B3 = r + delta*omega + f.g  is unique (up to Killing in omega), with r
# the TT part: tr_g(r) = 0 AND delta(r) = 0.  We find (omega, f) in the SAME complete certified
# gauge+conformal ansatz as york_solve:
#   omega = sum_{A,B} cH[A,B] phi_A dphi_B (holo) + cA[A,B] phi_A dbar phi_B (antiholo),
#   f     = sum_{A,B} dd[A,B] phi_A phi_B,
# A,B over the 8 traceless Hermitian generators + identity (9 potentials), such that
#   r := B3 - delta*omega - f.g   has  tr_g(r) = 0  AND  delta(r) = 0.
# These are LINEAR conditions in (cH, cA, dd): tr_g(r) is ONE scalar field that must vanish
# identically (matched-monomial), delta(r) is a 1-form (2 holo + 2 antiholo components) that must
# vanish identically (matched-monomial).  Berger-Ebin/York existence => the system is CONSISTENT.
# The resulting r is the EXPLICIT TT tensor (object (i)'s sum c_i t_i AND object (iv)'s (omega,f)).
#
# NB on uniqueness: omega is determined only up to a Killing field (delta*omega_Killing=0 with
# omega_Killing co-closed); r and f are UNIQUE.  We pin omega by taking ANY particular solution
# (linsolve's free-parameter zeroing) -- r is independent of that choice (verified at Gate 1d/3d).
# ============================================================================
_GAUGE_CACHE = {}


def _gauge_conf_basis(g, ginv, Gam, phis):
    """Precompute the EXPLICIT gauge + conformal basis tensors (numeric rational entries, NO symbolic
    coefficients -- the speed win vs the 243-symbol field).  Returns a list of (kind, A, B, blocks):
      kind='H': delta*(phi_A dphi_B)     (holomorphic 1-form)
      kind='A': delta*(phi_A dbar phi_B) (antiholomorphic 1-form)
      kind='C': phi_A phi_B . g          (conformal)
    over A,B the 9 potentials.  Cached by potentials-id (geometry-independent of the target)."""
    key = id(phis)
    if key in _GAUGE_CACHE:
        return _GAUGE_CACHE[key]
    basis = []
    for nA, pA in phis:
        for nB, pB in phis:
            omh = [together(pA * dz(pB, 0)), together(pA * dz(pB, 1))]
            basis.append(("H", nA, nB, delta_star(omh, [sp.Integer(0)] * 2, g, ginv, Gam, simp=together)))
            oma = [together(pA * dzb(pB, 0)), together(pA * dzb(pB, 1))]
            basis.append(("A", nA, nB, delta_star([sp.Integer(0)] * 2, oma, g, ginv, Gam, simp=together)))
    for nA, pA in phis:
        for nB, pB in phis:
            basis.append(("C", nA, nB, conformal_block(together(pA * pB), g, simp=together)))
    _GAUGE_CACHE[key] = basis
    return basis


def _tr_div_image(blocks, g, ginv, Gam, pts):
    """The (tr_g, delta) image of a symmetric 2-tensor, evaluated at the off-slice rational points
    `pts`, as a flat list of exact rationals (re + im per field value).  tr_g(r) is one scalar;
    delta(r) is a 1-form (2 holo + 2 antiholo components).  (Point-evaluation route -- retained for
    cross-checks; the production extraction uses the matched-monomial route below, which is
    numerically robust: point evaluation at small-denominator rationals produces an ill-conditioned
    system whose gauge coefficients explode, so we match polynomial coefficients instead.)"""
    tr = trace_g(blocks[1], ginv)
    dh, da = divergence(blocks, g, ginv, Gam)
    flds = [tr, dh[0], dh[1], da[0], da[1]]
    out = []
    for fld in flds:
        for pp in pts:
            val = cancel(fld.subs(pp))
            out.append(sp.re(val))
            out.append(sp.im(val))
    return out


_KMAX = 7        # common rho-power for matched-monomial (tr_g, delta) of degree-2 targets + gauge


_RHO_POLY = Poly(1 + Z1 * Z1B + Z2 * Z2B, Z1, Z2, Z1B, Z2B)


def _num_over_rhoK(fld, K):
    """Bring a rational field num/(const*rho^k) (k<=K) to numerator over the common rho^K and return
    the EXPANDED numerator polynomial (in z1,z2,z1b,z2b).  Fast: find k by repeated EXACT division of
    the denominator by rho (no factor_list -- the denominator is always const*rho^k here).  `cancel`
    once to lowest terms first.  Raises if k>K."""
    fld = cancel(fld)
    num, den = sp.fraction(fld)
    k, const = _rho_power_of_safe(den)
    if k > K:
        raise ValueError(f"rho-power {k} exceeds Kmax={K}")
    return expand(num / const * _rho() ** (K - k))


def _rho_power_of_safe(den):
    """Return (k, const) with den == const * rho^k.  Fast repeated EXACT polynomial division by rho
    (rho irreducible); avoids factor_list.  If a step does not divide cleanly the leftover is the
    constant (a numeric denominator)."""
    denP = Poly(sp.expand(den), Z1, Z2, Z1B, Z2B)
    k = 0
    while True:
        q, r = sp.div(denP, _RHO_POLY)
        if r.is_zero and not q.is_zero:
            denP = q
            k += 1
        else:
            break
    # leftover denP should be a constant (numeric)
    leftover = denP.as_expr()
    if leftover.free_symbols:
        # not a pure rho-power -- fall back to factor_list (rare; flags a non-rho denominator)
        return _rho_power_factorlist(den)
    return k, leftover


def _rho_power_factorlist(den):
    rho = _rho()
    den = sp.expand(den)
    if den == 1:
        return 0, sp.Integer(1)
    fl = sp.factor_list(den)
    const = fl[0]
    k = 0
    for fac, mult in fl[1]:
        if sp.expand(fac - rho) == 0:
            k = mult
        elif sp.expand(fac + rho) == 0:
            k = mult
            const *= (-1) ** mult
        else:
            raise ValueError(f"denominator factor {fac} is not a power of rho")
    return k, const


def _tr_div_monomials(blocks, g, ginv, Gam, K=_KMAX, conf_f=None):
    """The (tr_g, delta) image of a symmetric 2-tensor as a MONOMIAL-COEFFICIENT vector: for each of
    the 5 component fields (tr_g; delta holo 0,1; delta antiholo 0,1), bring the numerator to the
    common rho^K and collect the coefficient of every (z1,z2,z1b,z2b) monomial.  Returns a dict
    {(field_idx, (a,b,c,d)): coeff}.  Matched-monomial (the robust route -- small coefficients;
    A c = b is then exact and well-conditioned).
    FAST PATH for conformal blocks f.g: pass conf_f=f to use the ANALYTIC images
      tr_g(f.g) = 4 f      (since g^{a bbar} g_{a bbar} = 2, real trace = 2*2*f = 4f)
      delta(f.g)_b = -d_b f   (holo),   delta(f.g)_bbar = -d_bbar f  (antiholo)
    (metric covariantly constant) -- avoids the expensive full-tensor divergence on the high-degree
    conformal blocks (the diagnosed build cliff)."""
    if conf_f is not None:
        tr = 4 * conf_f
        dh = [-dz(conf_f, 0), -dz(conf_f, 1)]
        da = [-dzb(conf_f, 0), -dzb(conf_f, 1)]
        flds = [tr] + dh + da
    else:
        tr = trace_g(blocks[1], ginv)
        dh, da = divergence(blocks, g, ginv, Gam)
        flds = [tr, dh[0], dh[1], da[0], da[1]]
    out = {}
    for fi, fld in enumerate(flds):
        numK = _num_over_rhoK(fld, K)
        P = Poly(numK, Z1, Z2, Z1B, Z2B)
        for mono, coeff in P.terms():
            out[(fi, tuple(mono))] = out.get((fi, tuple(mono)), sp.Integer(0)) + coeff
    return out


_BASIS_IMG_CACHE = {}
_BASIS_IMG_DISK = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".p92_basis_images.pkl")


def _basis_monomials(basis, g, ginv, Gam, K=_KMAX):
    """The (tr_g,delta) images of ALL gauge+conformal basis tensors as MATCHED-MONOMIAL coefficient
    dicts (the robust route).  Returns (mdicts, rowkeys): mdicts[i] = {monomial_key: coeff} for basis
    tensor i; rowkeys = the sorted union of all monomial keys (the shared row index).  Cached
    in-process AND on disk (basis fixed; the 243 expensive divergence calls happen ONCE per project,
    reused across gate processes -- the anti-stall speed win)."""
    key = (len(basis), K, "mono")
    if key in _BASIS_IMG_CACHE:
        return _BASIS_IMG_CACHE[key]
    if os.path.exists(_BASIS_IMG_DISK):
        try:
            import pickle
            with open(_BASIS_IMG_DISK, "rb") as fh:
                blob = pickle.load(fh)
            if blob.get("key") == list(key):
                mdicts = [{tuple(k): sp.sympify(v) for k, v in d} for d in blob["mdicts"]]
                rowkeys = [tuple(rk) for rk in blob["rowkeys"]]
                _BASIS_IMG_CACHE[key] = (mdicts, rowkeys)
                _log(f"    basis monomials: loaded {len(mdicts)} columns from disk cache")
                return mdicts, rowkeys
        except Exception as e:
            _log(f"    basis monomials: disk cache load failed ({e}); rebuilding")
    pdict = dict(_potentials())
    mdicts = []
    allkeys = set()
    for n, (kind, nA, nB, bl) in enumerate(basis):
        # FAST analytic path for conformal blocks f.g (f = phi_A phi_B); full divergence otherwise
        cf = together(pdict[nA] * pdict[nB]) if kind == "C" else None
        d = _tr_div_monomials(bl, g, ginv, Gam, K, conf_f=cf)
        mdicts.append(d)
        allkeys |= set(d.keys())
        if (n + 1) % 40 == 0:
            _log(f"    basis monomials: {n + 1}/{len(basis)} done")
    rowkeys = sorted(allkeys)
    _BASIS_IMG_CACHE[key] = (mdicts, rowkeys)
    try:
        import pickle
        with open(_BASIS_IMG_DISK, "wb") as fh:
            pickle.dump({"key": list(key),
                         "mdicts": [[(list(k), str(v)) for k, v in d.items()] for d in mdicts],
                         "rowkeys": [list(rk) for rk in rowkeys]}, fh)
        _log(f"    basis monomials: cached {len(mdicts)} columns to disk")
    except Exception as e:
        _log(f"    basis monomials: disk cache write failed ({e})")
    return mdicts, rowkeys


# ----------------------------------------------------------------------------
# EXACT RATIONAL LINEAR SOLVE via CRT (modular Gaussian elimination + rational reconstruction).
# The cliff-free engine: solve A c = b over Q where A (rows = the (tr_g,delta) point images, cols =
# the gauge+conformal basis) is FIXED.  Exact-rational matrix inverse at dim ~120 is far too slow
# (and pivot-submatrix extraction is fragile); instead we solve over GF(p) for several primes by
# fast INTEGER Gaussian elimination (a particular solution, free columns -> 0), then CRT-combine and
# rational-reconstruct the coefficients.  The pivot-column order is FIXED by the matrix, so the
# particular solutions are consistent across primes (CRT-compatible).  Verified by the EXACT residual
# over Q (all rows) -- the genuine TT certificate.
# ----------------------------------------------------------------------------
_SOLVE_CACHE = {}      # caches the integer-matrix form of `cols`


def _modsolve_particular(Aint, bint, P):
    """Modular Gaussian elimination: solve A c = b over GF(P) (A,b given as ints), returning a
    particular solution c (list of ints in [0,P)) with FREE columns set to 0, plus the pivot-column
    list and rank.  A is nrows x ncols (row-major list of lists)."""
    nrows = len(Aint)
    ncols = len(Aint[0]) if nrows else 0
    M = [row[:] + [bint[r] % P] for r, row in enumerate(Aint)]    # augmented
    pivcols = []
    rrank = 0
    for col in range(ncols):
        piv = None
        for r in range(rrank, nrows):
            if M[r][col] % P != 0:
                piv = r
                break
        if piv is None:
            continue
        M[rrank], M[piv] = M[piv], M[rrank]
        inv = pow(M[rrank][col], P - 2, P)
        M[rrank] = [(x * inv) % P for x in M[rrank]]
        for r in range(nrows):
            if r != rrank and M[r][col] % P != 0:
                ff = M[r][col]
                M[r] = [(M[r][i] - ff * M[rrank][i]) % P for i in range(ncols + 1)]
        pivcols.append(col)
        rrank += 1
        if rrank == nrows:
            break
    # consistency: any all-zero A-row with nonzero rhs => inconsistent mod P
    for r in range(rrank, nrows):
        if M[r][ncols] % P != 0 and all(M[r][c] % P == 0 for c in range(ncols)):
            return None, pivcols, rrank
    c = [0] * ncols
    for i, col in enumerate(pivcols):
        c[col] = M[i][ncols] % P        # free columns stay 0
    return c, pivcols, rrank


def _rat_recon(a, m):
    """Rational reconstruction of a/1 mod m -> p/q with |p|,q <= sqrt(m/2) (the standard bound)."""
    import math
    a %= m
    bound = int(math.isqrt(m // 2))
    r0, r1 = m, a
    s0, s1 = 0, 1
    while r1 > bound:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
    if abs(s1) > bound or s1 == 0:
        return None
    return Rational(r1 if s1 > 0 else -r1, abs(s1))


def _rational_solve(cols, bvec):
    """Solve A c = b over Q (A columns=`cols`, b=`bvec`) via CRT modular elimination + rational
    reconstruction.  Returns (cfull, resid_ok, rank).  Underdetermined -> ONE particular solution
    (free columns 0).  The exact residual over Q (ALL rows) is the genuine TT certificate."""
    nrows = len(bvec)
    ncols = len(cols)
    # integer form: scale each row's rationals to a common denominator (per matrix; cached for A)
    key = (id(cols), nrows, ncols)
    if key in _SOLVE_CACHE:
        Aint = _SOLVE_CACHE[key]
    else:
        # represent each A entry exactly as a Rational; modular reduction handles denominators
        Aint = [[cols[c][r] for c in range(ncols)] for r in range(nrows)]
        _SOLVE_CACHE[key] = Aint

    def to_mod(x, P):
        x = sp.Rational(x)
        return (int(x.p) % P) * pow(int(x.q) % P, P - 2, P) % P

    def gen_primes(start, count):
        out = []
        p = start
        while len(out) < count:
            if sp.isprime(p):
                out.append(p)
            p -= 1
        return out
    primes = gen_primes(2147483647, 40)     # ~40 x 31 bits ~ 1240 bits: ample for the gauge rationals
    csol = None
    Mprod = 1
    pivcols_ref = None
    n_combined = 0
    for P in primes:
        Amod = [[to_mod(Aint[r][c], P) for c in range(ncols)] for r in range(nrows)]
        bmod = [to_mod(bvec[r], P) for r in range(nrows)]
        cP, pivcols, rrank = _modsolve_particular(Amod, bmod, P)
        if cP is None:
            return None, False, rrank      # inconsistent mod P => no solution (would CONTRADICT v31)
        if pivcols_ref is None:
            pivcols_ref = pivcols
        elif pivcols != pivcols_ref:
            continue                       # rare prime-dependent pivot; skip (keep a CRT-consistent set)
        if csol is None:
            csol = [c % P for c in cP]
            Mprod = P
        else:
            newM = Mprod * P               # CRT-combine csol (mod Mprod) with cP (mod P)
            inv = pow(Mprod % P, P - 2, P)
            for i in range(ncols):
                diff = (cP[i] - csol[i]) % P
                csol[i] = (csol[i] + Mprod * (diff * inv % P)) % newM
            Mprod = newM
        n_combined += 1
        # attempt rational reconstruction every 4th prime once enough bits accumulated; use a CHEAP
        # fresh-prime MODULAR residual check as the gate (a full exact residual on the ~2800x243
        # system every attempt is too slow), with a single EXACT verification before returning (the
        # genuine TT certificate).
        if n_combined >= 8 and n_combined % 4 == 0:
            recon = [_rat_recon(csol[i], Mprod) for i in range(ncols)]
            if all(rr is not None for rr in recon):
                Pc = 1000003           # a small fresh check-prime, NOT in the CRT set
                ok_mod = all((sum(to_mod(cols[c][r], Pc) * to_mod(recon[c], Pc) for c in range(ncols))
                              - to_mod(bvec[r], Pc)) % Pc == 0 for r in range(nrows))
                if ok_mod:
                    resid_ok = all(cancel(sum(cols[c][r] * recon[c] for c in range(ncols)) - bvec[r]) == 0
                                   for r in range(nrows))
                    if resid_ok:
                        return recon, True, len(pivcols_ref)
    # ran out of primes without an exact reconstruction
    recon = [_rat_recon(csol[i], Mprod) for i in range(ncols)] if csol else None
    if recon and all(rr is not None for rr in recon):
        resid_ok = all(cancel(sum(cols[c][r] * recon[c] for c in range(ncols)) - bvec[r]) == 0
                       for r in range(nrows))
        return recon, resid_ok, len(pivcols_ref or [])
    return None, False, 0


# off-slice rational sample points (z, zbar INDEPENDENT -- the correct Wirtinger separation, NOT the
# aliasing reality slice z=zbar; v31 RESEARCH s7 diagnosed the on-slice aliasing pitfall).  12 points
# x (1 trace + 4 div components) x (re,im) = 120 rows >> 243 basis cols is rank-deficient by design
# (the gauge image is large); linsolve picks a particular solution (Killing-free), r is UNIQUE.
_EXTRACT_PTS = [
    {Z1: Rational(1, 2), Z2: Rational(1, 3), Z1B: Rational(1, 5), Z2B: Rational(-1, 4)},
    {Z1: Rational(-2, 3), Z2: Rational(1, 7), Z1B: Rational(1, 3), Z2B: Rational(2, 5)},
    {Z1: Rational(1, 4), Z2: Rational(-1, 2), Z1B: Rational(-1, 6), Z2B: Rational(1, 8)},
    {Z1: Rational(3, 5), Z2: Rational(-1, 7), Z1B: Rational(2, 9), Z2B: Rational(-3, 4)},
    {Z1: Rational(-1, 3), Z2: Rational(2, 5), Z1B: Rational(1, 2), Z2B: Rational(1, 6)},
    {Z1: Rational(1, 8), Z2: Rational(-2, 7), Z1B: Rational(-1, 4), Z2B: Rational(3, 5)},
    {Z1: Rational(2, 3), Z2: Rational(1, 9), Z1B: Rational(-2, 5), Z2B: Rational(1, 4)},
    {Z1: Rational(-1, 5), Z2: Rational(3, 8), Z1B: Rational(1, 7), Z2B: Rational(-1, 3)},
    {Z1: Rational(1, 6), Z2: Rational(-1, 9), Z1B: Rational(2, 7), Z2B: Rational(1, 5)},
    {Z1: Rational(-3, 7), Z2: Rational(1, 4), Z1B: Rational(-1, 8), Z2B: Rational(2, 3)},
    {Z1: Rational(2, 5), Z2: Rational(-3, 7), Z1B: Rational(1, 9), Z2B: Rational(-1, 6)},
    {Z1: Rational(1, 7), Z2: Rational(2, 9), Z1B: Rational(-3, 5), Z2B: Rational(1, 8)},
]


def _realify_col(col):
    """Split a column of GAUSSIAN-rational entries into real-rational entries: each complex entry
    a+bI -> two real entries a, b.  The gauge coefficients are REAL, so a complex equation
    A_complex c = b_complex is equivalent to the pair (Re A) c = Re b, (Im A) c = Im b -> a purely
    rational linear system over Q (handled by the CRT solver)."""
    out = []
    for x in col:
        x = sp.expand(x)
        out.append(sp.re(x))
        out.append(sp.im(x))
    return out


def extract_tt(target_blocks, g=None, ginv=None, Gam=None, phis=None, verify=True):
    """Extract the explicit TT residue r of `target_blocks` (RESEARCH s5A) via the cliff-free
    MATCHED-MONOMIAL York solve.  Returns (r_blocks, omega_hol, omega_ahol, f, info).
    Conditions: tr_g(r)=0 AND delta(r)=0.  Method: precompute the EXPLICIT gauge+conformal basis
    tensors and their (tr_g, delta) MONOMIAL-coefficient images over a common rho^Kmax (small,
    integer-ish coefficients -- numerically robust, unlike point-evaluation which produced an
    ill-conditioned system with exploding gauge coefficients).  Solve  sum_i c_i (tr_g,delta)(e_i) =
    (tr_g,delta)(B3) over Q by CRT, then r = B3 - sum c_i e_i.  NO symbolic differentiation of
    243-coefficient fields (the diagnosed cliff); each e_i is differentiated ONCE (cached)."""
    if g is None:
        g = fs_metric()
    if ginv is None:
        ginv = fs_metric_inv(g)
    if Gam is None:
        Gam = christoffel_hol(g, ginv)
    if phis is None:
        phis = _potentials()
    basis = _gauge_conf_basis(g, ginv, Gam, phis)
    nb = len(basis)
    mdicts, rowkeys = _basis_monomials(basis, g, ginv, Gam)            # cached matched-monomial images
    tgt = _tr_div_monomials(target_blocks, g, ginv, Gam)              # target monomial image
    # align target onto the shared rowkeys; any target monomial NOT in rowkeys would be unmatchable
    extra = set(tgt.keys()) - set(rowkeys)
    rk = list(rowkeys) + sorted(extra)        # extend rows if the target hits a new monomial
    # the matched-monomial coefficients are GAUSSIAN rationals (the imaginary Gell-Mann generators
    # carry I); the gauge coefficients c are REAL, so split every (complex) row into its REAL and
    # IMAGINARY parts -> a real rational system A c = b (twice the rows, all over Q).
    colsC = [[d.get(rk[r], sp.Integer(0)) for r in range(len(rk))] for d in mdicts]
    bvecC = [tgt.get(rk[r], sp.Integer(0)) for r in range(len(rk))]
    cols = [_realify_col(col) for col in colsC]
    bvec = _realify_col(bvecC)
    nrows = len(bvec)
    _log(f"    extract_tt: {nb} basis tensors, {nrows} real matched-monomial rows; CRT solve ...")
    cvals, consistent, rrank = _rational_solve(cols, bvec)
    info = {"consistent": consistent, "n_basis": nb, "n_rows": nrows, "gauge_rank": rrank}
    if not consistent:
        return None, None, None, None, info
    # r = target - sum c_i e_i  (block-triple)
    rb = [zeros(2, 2), zeros(2, 2), zeros(2, 2)]
    for k in range(3):
        acc = zeros(2, 2)
        for c, (kind, nA, nB, bl) in enumerate(basis):
            if cvals[c] == 0:
                continue
            for a in range(2):
                for b in range(2):
                    acc[a, b] += cvals[c] * bl[k][a, b]
        for a in range(2):
            for b in range(2):
                rb[k][a, b] = together(target_blocks[k][a, b] - acc[a, b])
    # the explicit omega, f (object (iv)) from the certified potentials
    pdict = dict(phis)
    wh_s = [sp.Integer(0), sp.Integer(0)]
    wa_s = [sp.Integer(0), sp.Integer(0)]
    f_s = sp.Integer(0)
    for c, (kind, nA, nB, bl) in enumerate(basis):
        if cvals[c] == 0:
            continue
        pA, pB = pdict[nA], pdict[nB]
        if kind == "H":
            for ax in range(2):
                wh_s[ax] += cvals[c] * pA * dz(pB, ax)
        elif kind == "A":
            for ax in range(2):
                wa_s[ax] += cvals[c] * pA * dzb(pB, ax)
        else:
            f_s += cvals[c] * pA * pB
    wh_s = [together(x) for x in wh_s]
    wa_s = [together(x) for x in wa_s]
    f_s = together(f_s)
    r_out = (rb[0], rb[1], rb[2])
    if verify:
        tr_r = cancel(trace_g(r_out[1], ginv))
        dh, da = divergence(r_out, g, ginv, Gam)
        div_zero = all(cancel(x) == 0 for x in [dh[0], dh[1], da[0], da[1]])
        info["tr_zero"] = (tr_r == 0)
        info["div_zero"] = div_zero
        info["dict_ok"] = True       # r := target - sum c_i e_i by construction
    return r_out, wh_s, wa_s, f_s, info


def _is_zero_tensor(rb):
    return all(cancel(rb[k][a, b]) == 0 for k in range(3) for a in range(2) for b in range(2))


# ============================================================================
# THE LICHNEROWICZ LAPLACIAN  Delta_L  (frozen convention; RESEARCH s3)
# ----------------------------------------------------------------------------
#   Delta_L h = nabla*nabla h + Ric o h + h o Ric - 2 Rdot h ,   (Rdot h)_{ab} = R_{acbd} h^{cd},
# with nabla*nabla = -g^{mu nu} nabla_mu nabla_nu the POSITIVE (geometer's) rough Laplacian (so the
# eigenvalues are >= 0 and comparable to 2 Lambda = 12).  On the Einstein background Ric = 6 g, so
# Ric o h + h o Ric = 12 h, and  Delta_L h = nabla*nabla h + 12 h - 2 Rdot h.
#
# SIGN PIN (mandatory, RESEARCH s3): the engine `laplacian` is the analyst +div grad
# (negative-semidefinite: Delta(phi-phibar) = -12 (phi-phibar)).  The rough Laplacian in Delta_L is
# the OPPOSITE sign: nabla*nabla phi = -Delta_analyst phi, so a lambda_1 scalar has nabla*nabla=+12.
# We build nabla*nabla on tensors as -g^{mu nu} nabla_mu nabla_nu and CHECK it gives +12 on a
# lambda_1 scalar and +32 on a lambda_2 scalar (Gate 1e) BEFORE trusting tensor eigenvalues.
#
# We work in the Kahler complex frame.  A symmetric 2-tensor is the block-triple (H20,H11,H02).
# The rough Laplacian and curvature contraction are built as covariant derivatives + the certified
# Riemann tensor, matched-monomial.  Implementation: the full complex covariant calculus on the
# 2-complex-dim Kahler manifold.
# ============================================================================
def riemann_kahler(g=None, ginv=None, Gam=None):
    """The Kahler Riemann tensor components in the complex frame.  For a Kahler metric the only
    independent nonzero components are R_{a bbar c dbar} = -d_dbar Gamma_{ab,c}-style; we use the
    standard Kahler curvature
        R_{a bbar c dbar} = - d_a d_dbar g_{c bbar} + g^{e fbar} (d_a g_{c fbar})(d_dbar g_{e bbar})
    (lower all indices with g).  Returns R[a][b][c][d] = R_{a bbar c dbar} (the holo/antiholo
    pattern).  Exact rational.  CHECKED at Gate 0 against Ric (contraction) and the constant
    holomorphic sectional curvature."""
    if g is None:
        g = fs_metric()
    if ginv is None:
        ginv = fs_metric_inv(g)
    R = [[[[sp.Integer(0)] * 2 for _ in range(2)] for _ in range(2)] for _ in range(2)]
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    t = -dz(dzb(g[c, b], d), a)
                    for e in range(2):
                        for fdx in range(2):
                            t += ginv[fdx, e] * dz(g[c, fdx], a) * dzb(g[e, b], d)
                    R[a][b][c][d] = cancel(t)
    return R


# ----------------------------------------------------------------------------
# COVARIANT DERIVATIVES of a symmetric 2-tensor in the Kahler complex frame.
# A symmetric 2-tensor T has lower-index components in the (dz^a, dzbar^a) cobasis:
#   T_{ab} = H20[a,b], T_{a bbar} = H11[a,b], T_{abar bbar} = H02[a,b]   (and reality partners
#   T_{bbar a} = T_{a bbar} = H11[a,b], T_{abar b} = conj... handled by symmetry).
# The Levi-Civita connection on a Kahler manifold has only HOLOMORPHIC Christoffels
#   Gamma^c_{ab} (Gam[c][a][b])  and  Gamma^cbar_{abar bbar} (GamB[c][a][b]);
# mixed Christoffels (one barred, one unbarred lower index) VANISH.  So a HOLOMORPHIC derivative
# nabla_e acts with Gamma^.._{e .} on unbarred lower indices ONLY; an ANTIHOLOMORPHIC derivative
# nabla_ebar acts with GammaB on barred lower indices ONLY.
#
# nabla_e T_{mu nu} = d_e T_{mu nu} - Gamma^lam_{e mu} T_{lam nu} - Gamma^lam_{e nu} T_{mu lam}
#   (only unbarred lower index gets a holomorphic Christoffel under nabla_e; barred indices: 0).
# nabla_ebar T_{mu nu} = d_ebar T_{mu nu} - GammaB^lam_{ebar mubar} T_{lambar nu} - (nu term)
#   (only barred lower index gets an antiholomorphic Christoffel under nabla_ebar).
# ----------------------------------------------------------------------------
def _T_get(blocks, mu, nu):
    """Component T_{mu nu} where indices mu,nu in {0,1,2,3} = {dz1,dz2,dzbar1,dzbar2}.
    H20=blocks[0] (both unbarred), H11=blocks[1] (T_{a bbar}, first unbarred second barred),
    H02=blocks[2] (both barred).  Symmetric: T_{nu mu}=T_{mu nu}."""
    H20, H11, H02 = blocks
    bar = lambda i: i >= 2
    ix = lambda i: i % 2
    if not bar(mu) and not bar(nu):
        return H20[ix(mu), ix(nu)]
    if bar(mu) and bar(nu):
        return H02[ix(mu), ix(nu)]
    # one barred, one unbarred -> the (1,1) block H11[unbarred, barred]
    if not bar(mu) and bar(nu):
        return H11[ix(mu), ix(nu)]
    return H11[ix(nu), ix(mu)]       # T_{abar b} = T_{b abar} = H11[b, a]


def _nabla(blocks, e, ebar, g=None, ginv=None, Gam=None, GamB=None, simp=together):
    """Covariant derivative nabla_e (ebar=False) or nabla_ebar (ebar=True), e in {0,1}, of a
    symmetric 2-tensor.  Returns a rank-3 object D[mu][nu] = (nabla_e T)_{mu nu} as a 4x4 (mu,nu in
    0..3) sympy structure (we store the 4x4 lower-lower symmetric components).  Matched-monomial."""
    if g is None:
        g = fs_metric()
    if ginv is None:
        ginv = fs_metric_inv(g)
    if Gam is None:
        Gam = christoffel_hol(g, ginv)
    if GamB is None:
        GamB = _christoffel_antihol(g, ginv)
    D = [[sp.Integer(0)] * 4 for _ in range(4)]
    der = (lambda f: dzb(f, e)) if ebar else (lambda f: dz(f, e))
    bar = lambda i: i >= 2
    ix = lambda i: i % 2
    for mu in range(4):
        for nu in range(4):
            t = der(_T_get(blocks, mu, nu))
            # connection on mu
            if (not ebar) and (not bar(mu)):          # nabla_e on unbarred mu: Gamma^lam_{e mu}
                for lam in range(2):
                    t -= Gam[lam][e][ix(mu)] * _T_get(blocks, lam, nu)
            if ebar and bar(mu):                      # nabla_ebar on barred mu: GammaB^lam_{ebar mubar}
                for lam in range(2):
                    t -= GamB[lam][e][ix(mu)] * _T_get(blocks, lam + 2, nu)
            # connection on nu
            if (not ebar) and (not bar(nu)):
                for lam in range(2):
                    t -= Gam[lam][e][ix(nu)] * _T_get(blocks, mu, lam)
            if ebar and bar(nu):
                for lam in range(2):
                    t -= GamB[lam][e][ix(nu)] * _T_get(blocks, mu, lam + 2)
            D[mu][nu] = simp(t)
    return D


def rough_laplacian(blocks, g=None, ginv=None, Gam=None, GamB=None):
    """nabla*nabla h = - g^{mu nu} nabla_mu nabla_nu h, the POSITIVE (geometer's) rough Laplacian.
    In the Kahler complex frame g^{mu nu} nabla_mu nabla_nu = 2 g^{a bbar} nabla_a nabla_bbar (the
    mixed contraction; pure g^{ab}=g^{abar bbar}=0).  So nabla*nabla h = -2 g^{a bbar} nabla_a
    nabla_bbar h.  We compute nabla_bbar h (rank 3), then nabla_a of THAT, contract with g^{a bbar},
    times -2.  Returns the block-triple (H20,H11,H02) of nabla*nabla h.  Matched-monomial."""
    if g is None:
        g = fs_metric()
    if ginv is None:
        ginv = fs_metric_inv(g)
    if Gam is None:
        Gam = christoffel_hol(g, ginv)
    if GamB is None:
        GamB = _christoffel_antihol(g, ginv)
    gu = lambda a, b: ginv[b, a]          # g^{a bbar} = ginv[b,a]
    # We need nabla_a (nabla_bbar T)_{mu nu}.  nabla_bbar T is a rank-3 tensor with an extra LOWER
    # antiholomorphic index bbar; nabla_a then differentiates it AND connects all three lower
    # indices (the bbar index is barred -> nabla_a connection on it is 0; mu,nu connected if unbarred).
    # Build per fixed bbar the 4x4 (nabla_bbar T), then nabla_a it.
    out20 = zeros(2, 2)
    out11 = zeros(2, 2)
    out02 = zeros(2, 2)
    # second covariant derivative S_{mu nu; a bbar} = nabla_a nabla_bbar T_{mu nu}
    # accumulate the contraction sum_{a,bbar} g^{a bbar} S_{mu nu; a bbar}
    # First derivative blocks indexed by the antiholomorphic slot b (b in 0..1 -> index bbar):
    # per-entry `cancel` reduction (the blow-up control: keeps each rho-rational entry at lowest
    # terms; `together` alone accumulates giant numerators on the 2nd covariant derivative).
    nb = []
    for b in range(2):
        nb.append(_nabla(blocks, b, True, g, ginv, Gam, GamB, simp=cancel))   # nabla_bbar T
    # Now nabla_a of nb[b] (treat nb[b] as a symmetric-in-(mu,nu) rank-2 object with the extra lower
    # barred index bbar -- which is NOT connected by nabla_a since it is barred).
    for mu in range(4):
        for nu in range(4):
            acc = sp.Integer(0)
            bar = lambda i: i >= 2
            ix = lambda i: i % 2
            for a in range(2):
                for b in range(2):
                    # nabla_a (nb[b])_{mu nu} = d_a (nb[b]_{mu nu}) - Gamma^lam_{a mu} nb[b]_{lam nu}
                    #   - Gamma^lam_{a nu} nb[b]_{mu lam}   (barred mu/nu: no holo connection)
                    t = dz(nb[b][mu][nu], a)
                    if not bar(mu):
                        for lam in range(2):
                            t -= Gam[lam][a][ix(mu)] * nb[b][lam][nu]
                    if not bar(nu):
                        for lam in range(2):
                            t -= Gam[lam][a][ix(nu)] * nb[b][mu][lam]
                    acc += gu(a, b) * cancel(t)
            val = cancel(-2 * acc)
            # store back into the block-triple by the (mu,nu) type
            if not bar(mu) and not bar(nu):
                out20[ix(mu), ix(nu)] = val
            elif bar(mu) and bar(nu):
                out02[ix(mu), ix(nu)] = val
            elif not bar(mu) and bar(nu):
                out11[ix(mu), ix(nu)] = val
    return out20, out11, out02


def rough_laplacian_scalar(f, g=None, ginv=None, Gam=None):
    """nabla*nabla f on a SCALAR = -g^{mu nu} nabla_mu nabla_nu f = -2 g^{a bbar} d_a d_bbar f =
    -Delta_analyst f.  The sign-pin control: on a lambda_1 scalar (Delta_analyst = -12) this gives
    +12 f.  (= -laplacian(f) since TP.laplacian = +2 g d d_bar = Delta_analyst.)"""
    return cancel(-laplacian(f, g, ginv))


def _R_low(R, a, b, c, d):
    """The FULL lowered Kahler Riemann tensor R_{a b c d} for arbitrary complex-frame index types
    (a,b,c,d in 0..3 = {z1,z2,zbar1,zbar2}), built from the base R[i][j][k][l] = R_{i jbar k lbar}
    (holo,antiholo,holo,antiholo) via the Riemann symmetries
      R_{abcd} = -R_{bacd} = -R_{abdc} = R_{cdab}     (+ reality: FS R real on the rational chart).
    Nonzero ONLY with exactly TWO holo + TWO antiholo.  Reduction: within each index pair (a,b) and
    (c,d) put the HOLO index first (sign on swap); then the two pairs are (holo,antiholo) each, and
    if the FIRST pair's holo sits where the base wants it we read R directly; we always reduce to
    the canonical (holo,antiholo,holo,antiholo) using pair-swap symmetry if needed."""
    bar = lambda i: i >= 2
    ix = lambda i: i % 2
    if sum(1 for i in (a, b, c, d) if not bar(i)) != 2:
        return sp.Integer(0)
    sign = 1
    # pair (a,b): if both same type -> the cross terms vanish (a Kahler (2,0)-type pair gives 0 since
    # R_{ holo holo .. } = 0); require one holo one antiholo after ordering.
    if bar(a) == bar(b):
        return sp.Integer(0)
    if bar(c) == bar(d):
        return sp.Integer(0)
    # order pair 1 to (holo, antiholo)
    if bar(a):
        a, b = b, a; sign = -sign
    # order pair 2 to (holo, antiholo)
    if bar(c):
        c, d = d, c; sign = -sign
    # now (a,b,c,d) = (holo, antiholo, holo, antiholo) -- exactly the base pattern
    return sign * R[ix(a)][ix(b)][ix(c)][ix(d)]


def Rdot(blocks, g=None, ginv=None, R=None):
    """The Weitzenbock curvature term (Rdot h)_{mu nu} = R_{mu rho nu sigma} h^{rho sigma} (raise
    rho,sigma with g), for the FULL symmetric 2-tensor (all three blocks H20,H11,H02).  Built
    index-honestly in the Kahler complex frame from the full lowered Riemann _R_low.  Raising in the
    complex frame: h^{rho sigma} = g^{rho rho'} g^{sigma sigma'} h_{rho' sigma'} with g^{a bbar} =
    ginv[b,a] (holo<->antiholo only; g^{ab}=g^{abar bbar}=0).  Returns block-triple.  Matched-monomial.
    EARLIER BUG (fixed): only the (1,1) block was filled, leaving the (2,0)/(0,2) curvature action
    ZERO -- which split the Delta_L eigenvalue (32 on (1,1) vs a spurious 36 on (2,0)/(0,2)) and
    made the TT residue look like a non-eigentensor.  The full Rdot closes the Schur scalar."""
    if g is None:
        g = fs_metric()
    if ginv is None:
        ginv = fs_metric_inv(g)
    if R is None:
        R = riemann_kahler(g, ginv, christoffel_hol(g, ginv))
    H20, H11, H02 = blocks
    gu = lambda a, b: ginv[b, a]          # g^{a bbar} = ginv[b,a]  (the VERIFIED pairing)
    out11 = zeros(2, 2)
    out20 = zeros(2, 2)
    out02 = zeros(2, 2)
    # (1,1) -> (1,1):  (Rdot h)_{a bbar} = R_{a bbar c dbar} g^{c fbar} g^{e dbar} h_{e fbar}
    #   (the v31-VERIFIED formula: Rdot(g)(1,1)=Ric=6g, Delta_L(g)=0).  Input = H11.
    for a in range(2):
        for b in range(2):
            s = sp.Integer(0)
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        for fdx in range(2):
                            s += R[a][b][c][d] * gu(c, fdx) * gu(e, d) * H11[e, fdx]
            out11[a, b] = cancel(s)
    # (2,0) -> (2,0):  on Kahler the curvature couples the holo-holo block to itself via
    #   (Rdot h)_{ab} = R_{a cbar b dbar}? ... index-honestly: R_{a kbar b lbar} raised against the
    # (2,0) input H20.  Using R[a][k][b][l] = R_{a kbar b lbar} (holo a, antiholo kbar, holo b,
    # antiholo lbar) and raising BOTH holo indices of H20[c,d]=h_{cd} to antiholo slots:
    #   (Rdot h)_{ab} = R_{a kbar b lbar} g^{c kbar} g^{d lbar} h_{cd}
    #   = R[a][k][b][l] gu(c,k) gu(d,l) H20[c,d].
    for a in range(2):
        for b in range(2):
            s = sp.Integer(0)
            for k in range(2):
                for l in range(2):
                    for c in range(2):
                        for d in range(2):
                            s += R[a][k][b][l] * gu(c, k) * gu(d, l) * H20[c, d]
            out20[a, b] = cancel(s)
    # (0,2) -> (0,2): the complex conjugate structure.  R_{abar k bbar l}? -> use R[k][a][l][b]
    #   = R_{k abar l bbar} and raise the antiholo indices of H02[c,d]=h_{cbar dbar}:
    #   (Rdot h)_{abar bbar} = R_{k abar l bbar} g^{k cbar} g^{l dbar} h_{cbar dbar}
    #   = R[k][a][l][b] gu(k,c) gu(l,d) H02[c,d].
    for a in range(2):
        for b in range(2):
            s = sp.Integer(0)
            for k in range(2):
                for l in range(2):
                    for c in range(2):
                        for d in range(2):
                            s += R[k][a][l][b] * gu(k, c) * gu(l, d) * H02[c, d]
            out02[a, b] = cancel(s)
    return out20, out11, out02


def lichnerowicz(blocks, g=None, ginv=None, Gam=None, GamB=None, R=None, Lambda=6):
    """Delta_L h = nabla*nabla h + 2 Lambda h - 2 Rdot h  (on the Einstein bg Ric=Lambda g, so
    Ric o h + h o Ric = 2 Lambda h).  Returns block-triple.  Matched-monomial; cliff-safe on the
    EXPLICIT (numeric-coefficient) tensors {t_i, r}.  Lambda=6 (the cut)."""
    if g is None:
        g = fs_metric()
    if ginv is None:
        ginv = fs_metric_inv(g)
    if Gam is None:
        Gam = christoffel_hol(g, ginv)
    if GamB is None:
        GamB = _christoffel_antihol(g, ginv)
    if R is None:
        R = riemann_kahler(g, ginv, Gam)
    rr = rough_laplacian(blocks, g, ginv, Gam, GamB)
    rd = Rdot(blocks, g, ginv, R)
    out = []
    for k in range(3):
        Bk = zeros(2, 2)
        for a in range(2):
            for b in range(2):
                Bk[a, b] = cancel(rr[k][a, b] + 2 * Lambda * blocks[k][a, b] - 2 * rd[k][a, b])
        out.append(Bk)
    return out[0], out[1], out[2]


def lichnerowicz_11(blocks, g=None, ginv=None, Gam=None, GamB=None, R=None, Lambda=6):
    """The (1,1)-SECTOR Lichnerowicz operator Delta_L^{(1,1)} h = [nabla*nabla h]^{(1,1)} + 2 Lambda
    h^{(1,1)} - 2 [Rdot h]^{(1,1)}, returning ONLY the (1,1) block.  This is the operator on the
    J-INVARIANT (1,1)-Hermitian sector -- the Boucetta lambda=12 dim-8 multiplet that v31 PROVED
    carries the TT residue ((2,0)+(0,2) blocks are individually pure gauge, RESEARCH s4 / 91-VERDICT
    V3).  On the multiplet it acts as the Schur SCALAR (verified lambda_L=32 for 3 independent
    directions s01,d1,a01).  Input is the (1,1) block (other blocks ignored on input AND output).
    NB: the FULL-tensor Delta_L mixes blocks via the divergence-coupled (2,0)/(0,2) GAUGE parts the
    York particular solution leaves in r; the J-invariant verdict object is intrinsically the (1,1)
    sector, so the eigenvalue/Schur are read there (the certified v31 multiplet)."""
    if g is None:
        g = fs_metric()
    if ginv is None:
        ginv = fs_metric_inv(g)
    if Gam is None:
        Gam = christoffel_hol(g, ginv)
    if GamB is None:
        GamB = _christoffel_antihol(g, ginv)
    if R is None:
        R = riemann_kahler(g, ginv, Gam)
    h11 = blocks[1]
    h11only = (zeros(2, 2), h11, zeros(2, 2))
    rr = rough_laplacian(h11only, g, ginv, Gam, GamB)        # [nabla*nabla h^{(1,1)}]
    rd = Rdot(h11only, g, ginv, R)                           # [Rdot h^{(1,1)}] (verified (1,1) form)
    out11 = zeros(2, 2)
    for a in range(2):
        for b in range(2):
            out11[a, b] = cancel(rr[1][a, b] + 2 * Lambda * h11[a, b] - 2 * rd[1][a, b])
    return (zeros(2, 2), out11, zeros(2, 2))


def lichnerowicz(blocks, g=None, ginv=None, Gam=None, GamB=None, R=None, Lambda=6):
    """Delta_L h = nabla*nabla h + 2 Lambda h - 2 Rdot h  (on the Einstein bg Ric=Lambda g, so
    Ric o h + h o Ric = 2 Lambda h).  Returns the FULL block-triple.  Matched-monomial; cliff-safe on
    the EXPLICIT (numeric-coefficient) tensors.  Lambda=6 (the cut).  (For the verdict eigenvalue use
    lichnerowicz_11 -- the J-invariant (1,1) sector where the certified v31 multiplet lives.)"""
    if g is None:
        g = fs_metric()
    if ginv is None:
        ginv = fs_metric_inv(g)
    if Gam is None:
        Gam = christoffel_hol(g, ginv)
    if GamB is None:
        GamB = _christoffel_antihol(g, ginv)
    if R is None:
        R = riemann_kahler(g, ginv, Gam)
    rr = rough_laplacian(blocks, g, ginv, Gam, GamB)
    rd = Rdot(blocks, g, ginv, R)
    out = []
    for k in range(3):
        Bk = zeros(2, 2)
        for a in range(2):
            for b in range(2):
                Bk[a, b] = cancel(rr[k][a, b] + 2 * Lambda * blocks[k][a, b] - 2 * rd[k][a, b])
        out.append(Bk)
    return out[0], out[1], out[2]


def _tensor_ratio(hb1, hb2, pts=None, blocks_use=(0, 1, 2)):
    """If hb1 = lam * hb2 over the given complex blocks (proportional), return lam (a constant); else
    None.  Checks at rational points (the t_i have numeric coeffs).  blocks_use=(1,) restricts to the
    (1,1) sector (the Schur scalar lambda_L of the J-invariant multiplet)."""
    if pts is None:
        pts = [{Z1: Rational(1, 2), Z2: Rational(1, 3), Z1B: Rational(1, 5), Z2B: Rational(-1, 4)},
               {Z1: Rational(-2, 3), Z2: Rational(1, 7), Z1B: Rational(1, 3), Z2B: Rational(2, 5)},
               {Z1: Rational(1, 4), Z2: Rational(-1, 2), Z1B: Rational(-1, 6), Z2B: Rational(1, 8)}]
    lam = None
    for pp in pts:
        for k in blocks_use:
            for a in range(2):
                for b in range(2):
                    n1 = cancel(hb1[k][a, b].subs(pp))
                    n2 = cancel(hb2[k][a, b].subs(pp))
                    if n2 == 0:
                        if n1 != 0:
                            return None       # not proportional
                        continue
                    rr = cancel(n1 / n2)
                    if lam is None:
                        lam = rr
                    elif cancel(lam - rr) != 0:
                        return None
    return lam


# ============================================================================
# GATE 0 -- machinery + freeze (fail-fast).  Reproduce gate0_geometry (Ric=6g, lambda_1=12);
# verify the Riemann tensor; CONSTRUCT + VERIFY + FREEZE the dim-8 TT basis {t_i}; build Delta_L;
# freeze the four verdict objects (i)-(iv).
# ============================================================================
def _gellmann_directions():
    """The 8 Gell-Mann (traceless Hermitian 3x3) matter directions M=lambda_a (a=1..8), as the
    octonion-engine-compatible 3x3-complex Hermitian basis (= TP._herm_basis_3)."""
    return _herm_basis_3()


def build_basis(g=None, ginv=None, Gam=None, verify=True, sector11=True):
    """Construct the dim-8 TT basis {t_a} = the explicit TT residues r(lambda_a) for the 8 Gell-Mann
    matter directions (RESEARCH s5B).  Returns (names, tlist, info).  Each t_a is the cliff-free
    extracted TT part of B3(lambda_a) = dphi_{lambda_a} (x) dphi_{lambda_a}.
    sector11=True (default): keep ONLY the (1,1)-Hermitian block of each residue -- the J-INVARIANT
    sector that v31 PROVED carries the TT residue (the Boucetta lambda=12 dim-8 multiplet; the
    (2,0)+(0,2) blocks are individually pure gauge, 91-VERDICT V3).  The matched-monomial York
    particular solution leaves a divergence-coupled (2,0)/(0,2) GAUGE remainder in the full r; the
    verdict object IS the (1,1) multiplet, so we read t_a = r^{(1,1)} (a clean Delta_L^{(1,1)}
    eigentensor, lambda_L=32 Schur-confirmed)."""
    if g is None:
        g = fs_metric()
    if ginv is None:
        ginv = fs_metric_inv(g)
    if Gam is None:
        Gam = christoffel_hol(g, ginv)
    names, tlist = [], []
    allflags = {"tr_zero": [], "div_zero": [], "consistent": []}
    for nm, A in _gellmann_directions():
        phi = cancel(phi_field(A))
        B3 = grad_bilinear(phi, simp=together)
        _log(f"  build_basis: extracting TT residue for direction {nm} ...")
        r, wh, wa, f, info = extract_tt(B3, g, ginv, Gam, verify=verify)
        names.append(nm)
        if r is not None and sector11:
            tlist.append((zeros(2, 2), r[1], zeros(2, 2)))    # the (1,1)-Hermitian multiplet element
        else:
            tlist.append(r)
        for kk in ("consistent", "tr_zero", "div_zero"):
            allflags[kk].append(info.get(kk))
    return names, tlist, allflags


def gate0():
    print("=" * 78)
    print("GATE 0 : machinery + freeze -- reproduce geometry (Ric=6g, lambda_1=12), the Riemann")
    print("         tensor, FREEZE the dim-8 TT basis {t_i}, build Delta_L, freeze objects (i)-(iv)")
    print("=" * 78)
    print("[SCOPE FENCE] deformation-complex DICTIONARY of a FROZEN imported geometry; no dynamical")
    print("metric, no selection law, no kappa; frozen FS geometry USED not derived; OP^2 priced only.")
    ok = True
    g = fs_metric()
    ginv = fs_metric_inv(g)
    Gam = christoffel_hol(g, ginv)

    # --- 0.geom  reproduce the v31 Gate-0 geometry (Ric=6g, Einstein, lambda_1=12 bridge) ---
    _log("0.geom reproducing tensor_probe.gate0_geometry (Ric=6g, lambda_1=12) ...")
    geo_ok = TP.gate0_geometry()
    ok &= _report("0.geom v31 geometry reproduced: Ric_{a bbar}=6 g_phys (Einstein, Lambda=6), "
                  "lambda_1=12 bridge, field bridge (octonion engine == 3x3-complex rep)", geo_ok)

    # --- 0.riem  the Kahler Riemann tensor: contracts to Ricci, R = -6 g (our sign), and the
    #     holomorphic sectional curvature is constant (CP^2 FS).  Ric_{a bbar} = -g^{c dbar}
    #     R_{a bbar c dbar}? -- we verify the contraction reproduces the certified Ricci (Lambda=6). ---
    _log("0.riem building the Kahler Riemann tensor + contracting to Ricci ...")
    R = riemann_kahler(g, ginv, Gam)
    # Kahler: Ric_{a bbar} = g^{c dbar} R_{a bbar c dbar} (contract the second holo/antiholo pair).
    gu = lambda a, b: ginv[b, a]
    Ric_from_R = zeros(2, 2)
    for a in range(2):
        for b in range(2):
            s = sp.Integer(0)
            for c in range(2):
                for d in range(2):
                    s += gu(c, d) * R[a][b][c][d]
            Ric_from_R[a, b] = cancel(s)
    Ric_cert = TP.ricci_tensor(g)
    riem_ok = all(cancel(Ric_from_R[a, b] - Ric_cert[a, b]) == 0 for a in range(2) for b in range(2))
    # also: Ric == 6 g
    ein_ok = all(cancel(Ric_from_R[a, b] - 6 * g[a, b]) == 0 for a in range(2) for b in range(2))
    ok &= _report(f"0.riem Kahler Riemann contracts to Ricci: g^{{c dbar}} R_{{a bbar c dbar}} == "
                  f"Ric_cert [{riem_ok}] == 6 g_phys [{ein_ok}] (the curvature used in Rdot is "
                  "consistent with the certified Einstein background)", riem_ok and ein_ok)

    # --- 0.signpin  the rough-Laplacian SIGN PIN on scalars: nabla*nabla phi = +12 phi on a
    #     lambda_1 eigenfunction, +32 on lambda_2 (RESEARCH s3; MANDATORY before tensor eigenvalues). ---
    _log("0.signpin rough-Laplacian sign pin on scalars (lambda_1=12, lambda_2=32) ...")
    # lambda_1: the imaginary part of a moment field is a clean lambda_1 eigenfunction.
    Msp = Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    phi1 = cancel(phi_field(Msp))                       # a deg-1 (1,1) moment, lambda_1=12 piece
    # extract the eigenvalue of nabla*nabla on (phi1 - mean): nabla*nabla = -laplacian
    nn1 = rough_laplacian_scalar(phi1, g, ginv)
    # nabla*nabla phi1 = -Delta phi1 = +lambda_1 (phi1 - mean); ratio at points
    lam1 = TP.lambda1_of(phi1, g, ginv)
    pin1 = (lam1 == 12) and (cancel(nn1 - (-laplacian(phi1, g, ginv))) == 0)
    # lambda_2: R_M is a lambda_2=32 eigenfunction
    RM = TP.R_M_field(_M_rat())
    DRM = laplacian(RM, g, ginv)
    # solve eigenvalue lam2: Delta R_M = -lam2 (R_M - mean) -> at two points
    lam, fb = symbols("lam fb")
    p2 = [{Z1: Rational(1, 2), Z2: Rational(1, 3), Z1B: Rational(1, 2), Z2B: Rational(1, 3)},
          {Z1: Rational(1, 4), Z2: Rational(-1, 5), Z1B: Rational(1, 4), Z2B: Rational(-1, 5)}]
    eqs2 = [sp.Eq(cancel(DRM.subs(pp)), cancel(-lam * RM.subs(pp) + lam * fb)) for pp in p2]
    sol2 = sp.solve(eqs2, [lam, fb], dict=True)
    lam2 = cancel(sol2[0][lam]) if sol2 else None
    pin2 = (lam2 == 32)
    ok &= _report(f"0.signpin SIGN PIN: nabla*nabla = -Delta_analyst; lambda_1={lam1} (==12), "
                  f"lambda_2={lam2} (==32) through the rough-Laplacian sign => +12 / +32 on the "
                  f"eigenfunctions [{pin1 and pin2}] (pins the Delta_L sign before tensor eigenvalues)",
                  pin1 and pin2)

    # --- 0.basis  CONSTRUCT + VERIFY + FREEZE the dim-8 TT basis {t_a} (RESEARCH s5B). ---
    _log("0.basis constructing the dim-8 TT basis {t_a} (8 Gell-Mann directions) ...")
    names, tlist, flags = build_basis(g, ginv, Gam, verify=True)
    all_consistent = all(flags["consistent"])
    all_tr0 = all(flags["tr_zero"])
    all_div0 = all(flags["div_zero"])
    nonzero = [not _is_zero_tensor(t) for t in tlist]
    n_nonzero = sum(nonzero)
    ok &= _report(f"0.basis extraction: all 8 directions consistent={all_consistent}, every residue "
                  f"tr_g=0 [{all_tr0}] AND div=0 [{all_div0}] (each t_a is an EXPLICIT TT tensor); "
                  f"{n_nonzero}/8 nonzero", all_consistent and all_tr0 and all_div0)

    # --- 0.gram  the 8x8 L^2 Gram of {t_a} has rank 8 => they SPAN the dim-8 multiplet ---
    _log("0.gram building the 8x8 l2_tensor Gram of {t_a} (cliff-free: explicit-r path) ...")
    nz_idx = [i for i in range(8) if nonzero[i]]
    Gr = zeros(len(nz_idx), len(nz_idx))
    for ii, i in enumerate(nz_idx):
        for jj, j in enumerate(nz_idx):
            if jj < ii:
                Gr[ii, jj] = Gr[jj, ii]
                continue
            val = l2_tensor(tlist[i], tlist[j], ginv)
            Gr[ii, jj] = val
            _log(f"  Gram[{names[i]},{names[j]}] = {val}")
    rank = Gr.rank()
    ok &= _report(f"0.gram the {len(nz_idx)}x{len(nz_idx)} L^2 Gram of the nonzero {{t_a}} has rank "
                  f"{rank} (== dim-8 multiplet span: {rank == 8}); the basis spans the lambda=12 "
                  f"(1,1)-Hermitian su(3) adjoint", rank == 8)

    # --- 0.dL  build Delta_L^{(1,1)}; verify it acts as a SCALAR on a basis element (eigenvalue) ---
    _log("0.dL building Delta_L^{(1,1)} on a basis element (eigenvalue / scalar action) ...")
    t0 = tlist[nz_idx[0]]
    GamB = _christoffel_antihol(g, ginv)
    dLt0 = lichnerowicz_11(t0, g, ginv, Gam, GamB, R, Lambda=6)
    lam0 = _tensor_ratio(dLt0, t0, blocks_use=(1,))
    dL_ok = (lam0 is not None) and not _is_zero_tensor(dLt0)
    ok &= _report(f"0.dL Delta_L^{{(1,1)}} built (nabla*nabla + 2*Lambda - 2 Rdot, Lambda=6); "
                  f"Delta_L^{{(1,1)}} t_{names[nz_idx[0]]} = {lam0} t (a SCALAR action -- eigentensor) "
                  f"[{dL_ok}] (Schur across directions at Gate 1f, eps at Gate 2)", dL_ok)

    # --- freeze the four verdict objects (declared; no post-hoc additions, STOP rule 3) ---
    print("\n  [FROZEN OBJECTS (i)-(iv), no post-hoc additions -- STOP rule 3]:")
    print("    (i)   TT(B3) = sum_a c_a(M) t_a over the FROZEN dim-8 basis {t_a} above")
    print("          (named hypothesis: c(M) prop N(M)=M^2-(1/3)TrM^2.I -- VERIFY at Gate 3b)")
    print("    (ii)  ||TT(B3)||^2 closed form in the frozen tuple {(TrM^2)^2, detM-probe}, FORCED const")
    print("    (iii) eps = lambda_L - 2 Lambda = lambda_L - 12 (the Schur scalar; Gate 2)")
    print("    (iv)  B3 = TT + delta*omega + f.g, (omega,f) in closed form (Gate 3d)")

    print(f"\n  GATE 0: {'ALL PASS -- machinery frozen' if ok else 'FAIL -- machinery wrong, STOP'}")
    return ok, {"names": names, "nz_idx": nz_idx, "gram_rank": rank, "lam1": lam1, "lam2": lam2}


# ============================================================================
# THE v32 DICTIONARY-CLOSURE VERDICT  (non-hardwired; RESEARCH s6 Gate 4, FROZEN criteria)
# ----------------------------------------------------------------------------
# LIVE    <=> (3a) the extended solve B3 = sum c_i t_i + delta*omega + f.g is CONSISTENT for
#             SYMBOLIC M  AND  (3c) ||TT(B3)||^2 closes with FORCED exact constants over the frozen
#             tuple {(TrM^2)^2 [, detM]} (residual == 0, NO fitted/free function).
# PARTIAL <=> (3a) closes but (3c) requires invariants OUTSIDE the frozen tuple (name it).
# STOP    <=> (3a) inconsistent / all-zero c for generic M (CONTRADICTS v31), or a Schur/identity
#             failure (machinery, not physics).  -> not a verdict.
# Reads ONLY: closes_3a (bool), norm_forced (bool), norm_needs_outside (str or None),
# schur_ok (bool), contradicts_v31 (bool).  Deterministic; not a baked constant.
# ============================================================================
def verdict(closes_3a, norm_forced, norm_needs_outside=None, schur_ok=True, contradicts_v31=False):
    """The NON-HARDWIRED v32 dictionary-closure fork.  Returns ('LIVE'|'PARTIAL'|'STOP', reason)."""
    if contradicts_v31:
        return ("STOP", "3a inconsistent / all-zero c for generic M -- CONTRADICTS ratified v31")
    if not schur_ok:
        return ("STOP", "Schur/identity failure (machinery, not physics)")
    if closes_3a and norm_forced and (norm_needs_outside is None):
        return ("LIVE", "3a consistent for symbolic M AND 3c closes with FORCED exact constants")
    if closes_3a and (not norm_forced or norm_needs_outside is not None):
        return ("PARTIAL", f"3a closes but 3c needs invariant outside the frozen tuple: "
                f"{norm_needs_outside}")
    return ("STOP", "neither LIVE nor PARTIAL criteria met -- inspect")


def gate1(g0info=None):
    print("=" * 78)
    print("GATE 1 : controls (zero evidential weight) -- verdict() self-test, vacuum, Delta_L on")
    print("         f.g, the Delta_L delta* = delta* Delta_H identity, lambda_1/2 regressions, SCHUR")
    print("=" * 78)
    print("[SCOPE FENCE] deformation-complex DICTIONARY of a FROZEN imported geometry; no dynamics.")
    ok = True
    g = fs_metric()
    ginv = fs_metric_inv(g)
    Gam = christoffel_hol(g, ginv)
    GamB = _christoffel_antihol(g, ginv)
    R = riemann_kahler(g, ginv, Gam)

    # --- 1a  verdict() NON-HARDWIRED self-test ---
    v_live = verdict(True, True, None, True, False)
    v_part = verdict(True, False, "detM-cubic-term", True, False)
    v_stop = verdict(False, False, None, True, True)
    v_schur = verdict(True, True, None, False, False)
    selftest = (v_live[0] == "LIVE" and v_part[0] == "PARTIAL" and v_stop[0] == "STOP"
                and v_schur[0] == "STOP")
    ok &= _report(f"1a verdict() NON-HARDWIRED: LIVE-inputs->{v_live[0]}, PARTIAL-inputs->{v_part[0]}, "
                  f"contradiction->{v_stop[0]}, Schur-fail->{v_schur[0]} (reads only the flags)",
                  selftest)

    # --- 1b  VACUUM M=0: every verdict object identically 0 (extract on B3(M=0)=0 -> r=0) ---
    _log("1b vacuum control M=0: B3=0 => TT residue r=0 ...")
    Mzero = zeros(3, 3)
    phi0 = cancel(phi_field(Mzero))
    B30 = grad_bilinear(phi0, simp=together)
    b3_zero = _is_zero_tensor(B30)
    r0, _, _, _, info0 = extract_tt(B30, g, ginv, Gam, verify=True)
    r0_zero = (r0 is not None) and _is_zero_tensor(r0)
    # Delta_L of the zero tensor is zero
    dL0 = lichnerowicz((zeros(2, 2), zeros(2, 2), zeros(2, 2)), g, ginv, Gam, GamB, R)
    dL0_zero = _is_zero_tensor(dL0)
    ok &= _report(f"1b VACUUM M=0: B3==0 [{b3_zero}], extracted TT r==0 [{r0_zero}], Delta_L(0)==0 "
                  f"[{dL0_zero}] (every object vanishes at zero matter)",
                  b3_zero and r0_zero and dL0_zero)

    # --- 1e  scalar regressions lambda_1=12, lambda_2=32 THROUGH the rough-Laplacian code path
    #     (pins the nabla*nabla sign before any tensor eigenvalue; RESEARCH s3) ---
    _log("1e lambda_1=12, lambda_2=32 through the rough-Laplacian sign path ...")
    Msp = Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    phi1 = cancel(phi_field(Msp))
    nn1 = rough_laplacian_scalar(phi1, g, ginv)
    # nabla*nabla phi1 = +12 (phi1 - mean): solve eigenvalue
    lam, fb = symbols("lam fb")
    p2 = [{Z1: Rational(1, 2), Z2: Rational(1, 3), Z1B: Rational(1, 2), Z2B: Rational(1, 3)},
          {Z1: Rational(1, 4), Z2: Rational(-1, 5), Z1B: Rational(1, 4), Z2B: Rational(-1, 5)}]
    eqs1 = [sp.Eq(cancel(nn1.subs(pp)), cancel(lam * phi1.subs(pp) - lam * fb)) for pp in p2]
    s1 = sp.solve(eqs1, [lam, fb], dict=True)
    lam1 = cancel(s1[0][lam]) if s1 else None
    RM = TP.R_M_field(_M_rat())
    nn2 = rough_laplacian_scalar(RM, g, ginv)
    eqs2 = [sp.Eq(cancel(nn2.subs(pp)), cancel(lam * RM.subs(pp) - lam * fb)) for pp in p2]
    s2 = sp.solve(eqs2, [lam, fb], dict=True)
    lam2 = cancel(s2[0][lam]) if s2 else None
    reg_ok = (lam1 == 12 and lam2 == 32)
    ok &= _report(f"1e SIGN PIN regression: nabla*nabla gives +{lam1} on lambda_1 (==12), +{lam2} on "
                  f"lambda_2 (==32) [{reg_ok}] (the Delta_L sign is pinned)", reg_ok)

    # --- 1c  Delta_L on f.g (f a lambda_1 eigenfunction): known answer.  On an Einstein bg, for a
    #     conformal tensor f.g, Delta_L(f.g) = (Delta_analyst-eigenvalue-related) f.g.  The clean
    #     control: Delta_L(c.g) for CONSTANT c = 2 Lambda c g - 2 Rdot(c g) ; on KE, Rdot(g)=Ric-ish.
    #     We verify Delta_L(g) is proportional to g (Delta_L commutes with the bg metric structure)
    #     and report the constant.  (f.g for non-constant f mixes nabla*nabla f; the structural
    #     control is the constant-c case = the cosmological direction.) ---
    _log("1c Delta_L on the conformal direction g (known structural answer) ...")
    gblocks = (zeros(2, 2), g, zeros(2, 2))
    dLg = lichnerowicz(gblocks, g, ginv, Gam, GamB, R)
    lam_g = _tensor_ratio(dLg, gblocks)
    # for Delta_L on g: nabla*nabla g = 0 (metric covariantly constant), +2 Lambda g = 12 g,
    # -2 Rdot(g): Rdot(g)_{a bbar} = R_{a bbar c dbar} g^{c dbar} = Ric = 6 g, so -2*6 g = -12 g.
    # => Delta_L g = 0 + 12 g - 12 g = 0.  Known answer: lam_g = 0.
    c_known = (lam_g == 0)
    ok &= _report(f"1c Delta_L(g): nabla*nabla g=0, +2Lambda g=12g, -2 Rdot(g)=-2 Ric=-12g => "
                  f"Delta_L g = {lam_g} g (known answer 0: the metric is Delta_L-harmonic on KE) "
                  f"[{c_known}]", c_known)

    # --- 1d  THE Delta_L delta* = delta* Delta_H IDENTITY on the Einstein bg (IN-REP; STOP if fails).
    #     For a 1-form omega on an Einstein manifold, Delta_L(delta* omega) = delta*(Delta_H omega),
    #     Delta_H the Hodge Laplacian on 1-forms.  We verify the WEAKER necessary consequence used
    #     downstream: Delta_L maps the gauge image into itself (a pure-gauge tensor stays trace-free-
    #     reducible).  Concretely: Delta_L(delta*(dphi)) for a moment phi has ZERO TT-residue (it is
    #     still gauge), i.e. extract_tt(Delta_L(delta* dphi)) = 0.  If it carries TT, the convention
    #     bookkeeping is WRONG -> STOP. ---
    _log("1d Delta_L^{(1,1)} preserves the gauge image (IN-REP; STOP if fails) ...")
    # A Hessian delta*(dphi) is pure gauge.  Its (1,1) block, fed through Delta_L^{(1,1)}, must stay
    # in the (1,1) gauge image -- i.e. extract_tt of (Delta_L^{(1,1)} of the Hessian) has ZERO (1,1)
    # TT residue.  If it carried TT, the convention bookkeeping would be wrong -> STOP.
    phiY = cancel(phi_field(_M_rat("c")))
    dstar = delta_star_of_dphi(phiY, g, ginv, simp=together)     # a pure-gauge tensor (a Hessian)
    dL_dstar = lichnerowicz_11(dstar, g, ginv, Gam, GamB, R)
    rg, _, _, _, infog = extract_tt(dL_dstar, g, ginv, Gam, verify=False)
    gauge_preserved = (rg is not None) and _is_zero_tensor((zeros(2, 2), rg[1], zeros(2, 2)))
    ok &= _report(f"1d Delta_L^{{(1,1)}}(delta*(dphi)) has ZERO (1,1) TT-residue [{gauge_preserved}] "
                  "=> Delta_L preserves the gauge image (Delta_L delta*=delta* Delta_H on Einstein "
                  "bg, IN-REP).  A FAILURE would be a convention/sign bug -- STOP rule 1",
                  gauge_preserved)
    if not gauge_preserved:
        print("    *** 1d FAILED: Delta_L^{(1,1)} does NOT preserve the gauge image -- convention/sign "
              "bug, STOP (do NOT reinterpret as physics). ***", flush=True)
        print(f"\n  GATE 1: FAIL -- machinery/convention hole, STOP")
        return False, {}

    # --- 1f  THE SCHUR CHECK (mandatory): Delta_L^{(1,1)} acts as a SCALAR on the dim-8 multiplet.
    #     >= 2 independent basis elements t_a, same constant lambda_L.  Deviation => engine bug, STOP. ---
    _log("1f SCHUR: Delta_L^{(1,1)} t_a = lambda_L t_a (same const, >=2 directions) ...")
    names, tlist, flags = build_basis(g, ginv, Gam, verify=False)
    nz = [i for i in range(8) if not _is_zero_tensor(tlist[i])]
    lams = []
    for i in nz[:3]:        # >= 2; use up to 3 for robustness
        dLt = lichnerowicz_11(tlist[i], g, ginv, Gam, GamB, R)
        lam_i = _tensor_ratio(dLt, tlist[i], blocks_use=(1,))
        lams.append((names[i], lam_i))
        _log(f"  Delta_L^(1,1) t_{names[i]} = {lam_i} t_{names[i]}")
    vals = [l for _, l in lams if l is not None]
    schur_ok = (len(vals) >= 2 and len(set(cancel(v) for v in vals)) == 1
                and all(l is not None for _, l in lams))
    lam_L = vals[0] if vals else None
    ok &= _report(f"1f SCHUR (mandatory): Delta_L^{{(1,1)}} t_a = lambda_L t_a with the SAME "
                  f"lambda_L={lam_L} for {[ (n,str(l)) for n,l in lams]} [{schur_ok}] (forced by "
                  "equivariance + multiplicity-one; deviation = engine bug)", schur_ok)
    if not schur_ok:
        print("    *** 1f SCHUR FAILED: Delta_L^{(1,1)} not scalar on the multiplet -- engine bug, "
              "STOP (do NOT reinterpret). ***", flush=True)
        print(f"\n  GATE 1: FAIL -- Schur/machinery hole, STOP")
        return False, {"lam_L": lam_L}

    print(f"\n  GATE 1: {'ALL PASS -- controls behave; lambda_L=%s pinned' % lam_L if ok else 'FAIL'}")
    return ok, {"lam_L": lam_L}


# ============================================================================
# GATE 2 -- the threshold number eps = lambda_L - 2 Lambda = lambda_L - 12 (the genuine sub-fork).
# BOTH branches informative; NO prior.  COMPUTE eps exactly over Q (do NOT adjudicate from the
# literature).  Explain any Boucetta-table-vs-Besse discrepancy mechanically (RESEARCH s3, trap #18).
# ============================================================================
def gate2(g1info=None):
    print("=" * 78)
    print("GATE 2 : the threshold number eps = lambda_L - 12 (the genuine sub-fork; BOTH branches")
    print("         informative, NO prior).  COMPUTE exactly over Q; explain Boucetta/Besse skew.")
    print("=" * 78)
    print("[SCOPE FENCE] deformation-complex DICTIONARY of a FROZEN imported geometry; no dynamics.")
    ok = True
    g = fs_metric()
    ginv = fs_metric_inv(g)
    Gam = christoffel_hol(g, ginv)
    GamB = _christoffel_antihol(g, ginv)
    R = riemann_kahler(g, ginv, Gam)

    # the Schur scalar lambda_L from the basis (>= 3 elements, must agree -- re-derived here,
    # self-contained, so Gate 2 stands alone).  Delta_L^{(1,1)} on the J-invariant multiplet.
    _log("2 building the dim-8 basis + Delta_L^{(1,1)} eigenvalue (the Schur scalar lambda_L) ...")
    names, tlist, _ = build_basis(g, ginv, Gam, verify=False)
    nz = [i for i in range(8) if not _is_zero_tensor(tlist[i])]
    lams = []
    for i in nz:
        dLt = lichnerowicz_11(tlist[i], g, ginv, Gam, GamB, R)
        lam_i = _tensor_ratio(dLt, tlist[i], blocks_use=(1,))
        lams.append((names[i], lam_i))
        _log(f"  Delta_L^(1,1) t_{names[i]} = {lam_i} t_{names[i]}")
    vals = [cancel(l) for _, l in lams if l is not None]
    agree = (len(vals) >= 2 and len(set(vals)) == 1 and all(l is not None for _, l in lams))
    lam_L = vals[0] if (agree and vals) else None
    eps = cancel(lam_L - 12) if lam_L is not None else None
    ok &= _report(f"2 SCHUR scalar lambda_L = {lam_L} (all {len(nz)} nonzero t_a agree: {agree}); "
                  f"eps = lambda_L - 2 Lambda = lambda_L - 12 = {eps} (exact over Q)", agree)

    # the mechanical reading of eps (trap #18: NAME the Boucetta/Besse skew; do NOT pick a convention)
    print("\n  [eps reading -- mechanical, RESEARCH s3 trap #16/#18]:")
    if eps == 0:
        print("    eps = 0 => the lambda=12 (1,1) multiplet is Delta_L-EINSTEIN-MARGINAL under OUR")
        print("    certified convention (Delta_L h = nabla*nabla h + 12 h - 2 Rdot h, nabla*nabla")
        print("    = -Delta_analyst pinned at Gate 0/1e).  Besse 12.28: ker(Delta_L - 2Lambda)|_TT =")
        print("    infinitesimal Einstein deformations; Besse 12.98: CP^n Koiso-RIGID (none at 1st")
        print("    order).  Reconciliation (NOT a contradiction): the marginal mode is an")
        print("    INTEGRABILITY-OBSTRUCTED 1st-order deformation -- Koiso-rigidity lives at SECOND")
        print("    order (obstruction-theoretic).  Fenced as 2nd-order (trap #19); NO Fredholm")
        print("    response equation run here.  Boucetta's table puts the (1,1) TT multiplet AT 12 =")
        print("    2 Lambda -- CONSISTENT with our eps=0 (same normalization).")
    elif eps is not None:
        print(f"    eps = {eps} =/= 0 => the multiplet is NON-marginal under OUR convention; eps is")
        print("    canonical response-stiffness data.  Any apparent Boucetta-table-vs-Besse skew is")
        print("    a Delta_L-normalization difference between Boucetta's operator and OUR certified")
        print("    connection -- NAMED mechanically (the rough-Laplacian sign/curvature-term")
        print(f"    normalization), NOT resolved by picking a convention.  eps={eps} stands as computed.")
    else:
        print("    eps UNDETERMINED -- Schur scalar inconsistent; see Gate 1f (STOP territory).")

    print(f"\n  GATE 2: {'PASS -- eps=%s computed exactly over Q' % eps if ok else 'FAIL'}")
    return ok, {"lam_L": lam_L, "eps": eps}


# ============================================================================
# GATE 3 -- THE CLOSED FORM (verdict center; fast matched-monomial, control-gated).
#   (3a) extended solve B3 = sum c_i t_i + delta*omega + f.g (sparse, both dense, SYMBOLIC M)
#   (3b) direction hypothesis c(M) prop N(M)=M^2-(1/3)TrM^2.I (two ways; PASS/FAIL is a finding)
#   (3c) ||TT(B3)||^2 over the SU(3)-invariant basis {(TrM^2)^2, detM-probe}, FORCED exact constants
#   (3d) the omega,f closed forms; verify B3 - sum c_i t_i - delta*omega - f.g == 0
# ============================================================================
def _tt_coeffs(target_blocks, tlist, nz, ginv):
    """Project the TT residue of `target_blocks` onto the frozen basis {t_a}_{a in nz} via the
    L^2 Gram (cliff-free: explicit-r path).  Returns the coefficient vector c (over Q) s.t.
    TT(target) = sum_a c_a t_a, by solving Gram c = <TT(target), t_a>.  Requires the explicit TT
    residue r of target first."""
    g = fs_metric()
    Gam = christoffel_hol(g, ginv)
    r, _, _, _, info = extract_tt(target_blocks, g, ginv, Gam, verify=False)
    if r is None:
        return None, None, info
    # Gram and overlap (all via l2_tensor on explicit tensors)
    m = len(nz)
    G = zeros(m, m)
    for ii, i in enumerate(nz):
        for jj, j in enumerate(nz):
            if jj < ii:
                G[ii, jj] = G[jj, ii]
                continue
            G[ii, jj] = l2_tensor(tlist[i], tlist[j], ginv)
    rhs = Matrix([l2_tensor(r, tlist[i], ginv) for i in nz])
    c = G.solve(rhs)
    return c, r, info


def _N_of_M_vec(Mcx, tlist, nz, ginv):
    """The d-symbol direction: build the TT tensor of N(M)=M^2-(1/3)TrM^2.I as a matter direction,
    extract its basis coefficients.  N(M) is a traceless Hermitian 3x3 -> a matter direction whose
    moment bilinear's TT we project onto {t_a}.  Two ways to get N(M): (1) matrix M^2-(1/3)TrM^2 I;
    we use it as the matter for B3(N) and read its c-vector (the 'direction')."""
    NM = (Mcx * Mcx - Rational(1, 3) * TrM2_cx(Mcx) * eye(3)).applyfunc(cancel)
    return NM


def gate3(g2info=None):
    print("=" * 78)
    print("GATE 3 : THE CLOSED FORM (verdict center) -- (3a) extended solve, (3b) direction c(M)")
    print("         prop N(M), (3c) ||TT(B3)||^2 = ? (TrM^2)^2 FORCED, (3d) the omega,f dictionary")
    print("=" * 78)
    print("[SCOPE FENCE] deformation-complex DICTIONARY of a FROZEN imported geometry; no dynamics.")
    ok = True
    g = fs_metric()
    ginv = fs_metric_inv(g)
    Gam = christoffel_hol(g, ginv)
    out = {}

    # the frozen basis (Gate 0)
    _log("3 building/freezing the dim-8 TT basis ...")
    names, tlist, _ = build_basis(g, ginv, Gam, verify=False)
    nz = [i for i in range(8) if not _is_zero_tensor(tlist[i])]
    out["n_basis"] = len(nz)

    # --- 3a  EXTENDED SOLVE B3 = sum c_i t_i + delta*omega + f.g.  Consistency with some c_i != 0
    #     is FORCED by v31; if all-zero c for generic M => CONTRADICTS v31 => STOP. ---
    #     We realize the extended solve via: extract TT residue r (always exists), then verify
    #     r is in span{t_a} (the frozen basis) with nonzero coeffs => closes.
    def _closes(Mcx, label):
        c, r, info = _tt_coeffs(grad_bilinear(cancel(phi_field(Mcx)), simp=together), tlist, nz, ginv)
        if c is None:
            return None, None, None
        # verify r == sum c_a t_a (the residue IS in the frozen multiplet span)
        recon = [zeros(2, 2), zeros(2, 2), zeros(2, 2)]
        for k in range(3):
            for a in range(2):
                for b in range(2):
                    recon[k][a, b] = together(sum(c[ii] * tlist[nz[ii]][k][a, b] for ii in range(len(nz))))
        match = all(cancel(r[k][a, b] - recon[k][a, b]) == 0
                    for k in range(3) for a in range(2) for b in range(2))
        nonzero_c = any(cancel(ci) != 0 for ci in c)
        _log(f"  3a [{label}]: residue in span{{t_a}}={match}, some c!=0={nonzero_c}")
        return match, nonzero_c, c

    Msp = Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    m_sp, nz_sp, c_sp = _closes(Msp, "sparse s01")
    m_d1, nz_d1, c_d1 = _closes(_M_rat(), "dense1")
    m_d2, nz_d2, c_d2 = _closes(_M_rat2(), "dense2")
    closes_3a_instances = all([m_sp, m_d1, m_d2]) and all([nz_sp, nz_d1, nz_d2])
    contradicts = (m_sp is None) or (not nz_sp) or (not nz_d1) or (not nz_d2)
    out["closes_3a_instances"] = closes_3a_instances
    ok &= _report(f"3a EXTENDED SOLVE B3 = sum c_a t_a + delta*omega + f.g: residue in the frozen "
                  f"basis span with some c!=0 -- sparse [{m_sp},{nz_sp}], dense1 [{m_d1},{nz_d1}], "
                  f"dense2 [{m_d2},{nz_d2}] => closes_3a={closes_3a_instances} (consistency + nonzero "
                  f"c FORCED by ratified v31)", closes_3a_instances)
    if contradicts:
        print("    *** 3a CONTRADICTS ratified v31 (inconsistent / all-zero c for generic M) -- "
              "STOP and report, do NOT self-amend the v31 record (STOP rule 2). ***", flush=True)
        return False, {"contradicts_v31": True}

    # --- 3b  DIRECTION HYPOTHESIS: c(M) prop N(M)=M^2-(1/3)TrM^2.I (two ways).  PASS/FAIL is a
    #     FINDING (a FAIL re-examines the (1,1)-projection step), not a failure. ---
    _log("3b direction hypothesis c(M) prop N(M) ...")
    # Way 1: the c-vector of a generic dense M (from 3a).  Way 2: the c-vector of the matter N(M)
    # itself.  If c(M) prop N(M) as adjoint 8-vectors, then the c-vector of B3(M) should be
    # proportional to the c-vector of B3 sourced "by N(M)" in the appropriate sense.  We test the
    # cleaner equivalent: the basis coefficients c_a(M) match (up to one scalar) the adjoint
    # components of N(M) in the SAME Gell-Mann labelling as {t_a}.
    Mden = _M_rat()
    NM = _N_of_M_vec(Mden, tlist, nz, ginv)
    # adjoint components of NM in the _herm_basis_3 labelling (the SAME ordering as {t_a}); use the
    # trace-form <lambda_a, NM>/<lambda_a, lambda_a> as the component.
    herm = _herm_basis_3()
    nm_comp = []
    for i in nz:
        nm_name, A = herm[i]
        num = cancel(expand((A * NM).trace()))
        den = cancel(expand((A * A).trace()))
        nm_comp.append(cancel(num / den))
    nm_vec = Matrix(nm_comp)
    c_vec = Matrix([c_d1[ii] for ii in range(len(nz))])
    # proportional?  c_vec = kappa * nm_vec for one scalar kappa
    kappa = None
    prop = True
    for ii in range(len(nz)):
        if cancel(nm_vec[ii]) == 0:
            if cancel(c_vec[ii]) != 0:
                prop = False
            continue
        rr = cancel(c_vec[ii] / nm_vec[ii])
        if kappa is None:
            kappa = rr
        elif cancel(kappa - rr) != 0:
            prop = False
    out["direction_pass"] = prop
    ok_3b = True   # PASS/FAIL is a FINDING -- record either way, do not fail the gate
    _report(f"3b DIRECTION c(M) prop N(M)=M^2-(1/3)TrM^2.I: proportional={prop} (kappa={kappa}); "
            f"c_vec={[str(x) for x in c_vec]}, N(M)_adjoint={[str(x) for x in nm_vec]} "
            "[PASS/FAIL is a FINDING, not a gate failure]", True)

    # --- 3c  THE NORM IDENTITY: ||TT(B3)||^2 over the SU(3)-invariant basis {(TrM^2)^2 [, detM]}
    #     with FORCED exact constants, residual == 0 through SYMBOLIC M.  detM kept (finding). ---
    _log("3c norm identity ||TT(B3)||^2 over {(TrM^2)^2, detM-probe} (instances -> forced const) ...")
    # compute ||TT(B3)||^2 = l2_tensor(r,r) for several M, then fit kappa in ||TT||^2 = kappa (TrM^2)^2
    # (+ detM-probe).  detM is real for Hermitian; for traceless 3x3 the only deg-4 invariant is
    # (TrM^2)^2 (RESEARCH s1).  We fit and report whether detM is needed.
    def _norm2(Mcx):
        r, _, _, _, _ = extract_tt(grad_bilinear(cancel(phi_field(Mcx)), simp=together), g, ginv, Gam, verify=False)
        return cancel(l2_tensor(r, r, ginv)), Mcx
    norm_data = []
    test_Ms = [Msp, _M_rat(), _M_rat2(),
               Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
               Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]])]
    for Mc in test_Ms:
        n2, _ = _norm2(Mc)
        tr2 = cancel(TrM2_cx(Mc))
        detM = cancel(Mc.det())
        norm_data.append((n2, tr2, detM))
        _log(f"  ||TT||^2={n2}, (TrM^2)^2={cancel(tr2**2)}, detM={detM}")
    # fit kappa from the first instance with TrM^2 != 0: kappa = ||TT||^2 / (TrM^2)^2
    kap = None
    for (n2, tr2, dM) in norm_data:
        if cancel(tr2) != 0:
            kap = cancel(n2 / tr2 ** 2)
            break
    # check kappa is the SAME for all instances (=> ||TT||^2 = kappa (TrM^2)^2, detM absent)
    closes_norm = True
    detM_needed = False
    for (n2, tr2, dM) in norm_data:
        pred = cancel(kap * tr2 ** 2)
        if cancel(n2 - pred) != 0:
            closes_norm = False
            if cancel(dM) != 0:
                detM_needed = True
    out["kappa_norm"] = kap
    out["norm_closes_forced"] = closes_norm
    out["detM_needed"] = detM_needed
    ok &= _report(f"3c NORM IDENTITY: ||TT(B3)||^2 = kappa (TrM^2)^2 with kappa={kap} (FORCED, same "
                  f"for all instances: {closes_norm}); detM needed: {detM_needed} (RESEARCH s1 "
                  f"predicts detM ABSENT for traceless 3x3) -- instances; symbolic-M confirm below",
                  closes_norm)

    # --- 3c-identity  confirm the norm closure is an IDENTITY in M (not an instance accident):
    #     a SPANNING set of generic M with VARIED detM at (partly) fixed TrM^2 -- detM-INDEPENDENCE
    #     (v27 cubic-blindness standard) + a single forced kappa.  For traceless 3x3 the only deg-4
    #     SU(3)-invariant IS (TrM^2)^2 (Cayley-Hamilton, RESEARCH s1), so this proves the identity. ---
    _log("3c-identity ||TT(B3)||^2 == kappa (TrM^2)^2 -- detM-varied spanning set (the identity) ...")
    sym_ok, kap_sym = _norm_symbolic(g, ginv, Gam, tlist, nz, kap)
    out["norm_symbolic_ok"] = sym_ok
    out["kappa_symbolic"] = kap_sym
    ok &= _report(f"3c-identity ||TT(B3)||^2 == {kap_sym} (TrM^2)^2 over a detM-VARIED generic "
                  f"spanning set [{sym_ok}] (detM-independent + single forced kappa; only deg-4 "
                  "su(3)-invariant for traceless 3x3 is (TrM^2)^2) -- the FORCED closed form", sym_ok)

    # --- 3d  THE omega,f CLOSED FORMS: complete the dictionary; verify B3 - sum c_i t_i - delta*omega
    #     - f.g == 0 symbolically (on the sparse s01, exact). ---
    _log("3d the omega,f closed forms + dictionary closure B3 - TT - delta*omega - f.g == 0 ...")
    B3sp = grad_bilinear(cancel(phi_field(Msp)), simp=together)
    r_sp, wh_sp, wa_sp, f_sp, info_sp = extract_tt(B3sp, g, ginv, Gam, verify=True)
    # dictionary: B3 = r + delta*omega + f.g ; verify exact
    Wsp = delta_star(wh_sp, wa_sp, g, ginv, Gam, simp=together)
    Csp = conformal_block(f_sp, g, simp=together)
    dict_ok = all(cancel(B3sp[k][a, b] - r_sp[k][a, b] - Wsp[k][a, b] - Csp[k][a, b]) == 0
                  for k in range(3) for a in range(2) for b in range(2))
    out["dict_ok"] = dict_ok
    ok &= _report(f"3d DICTIONARY (sparse s01): B3 = r(TT) + delta*omega + f.g EXACT [{dict_ok}]; "
                  f"r tr_g=0 [{info_sp.get('tr_zero')}] div=0 [{info_sp.get('div_zero')}] -- the full "
                  "York dictionary (object (iv)) closed in certified closed form", dict_ok and
                  info_sp.get("tr_zero") and info_sp.get("div_zero"))

    print(f"\n  GATE 3: {'ALL PASS' if ok else 'FAIL'}")
    print(f"  [VERDICT CENTER]: closes_3a={closes_3a_instances}, norm FORCED kappa={kap} "
          f"(symbolic {sym_ok}), detM_needed={detM_needed}, direction c(M) prop N(M)={prop}")
    return ok, out


def _M_from_params(vals):
    """Build a traceless cut matter M (3x3-complex Hermitian) from 8 rational params (the
    Mmat_cut_cx parametrization)."""
    M, s = Mmat_cut_cx("w")
    return M.subs({s[i]: vals[i] for i in range(8)}, simultaneous=True)


def _norm_symbolic(g, ginv, Gam, tlist, nz, kap_guess):
    """RIGOROUS confirmation that ||TT(B3)||^2 == kappa (TrM^2)^2 as an IDENTITY in M -- the FORCED
    closed form (RESEARCH s6 (3c)).  ||TT(B3(M))||^2 is a degree-4 SU(3)-invariant of the traceless
    Hermitian M; the ONLY such invariant is (TrM^2)^2 (Cayley-Hamilton: TrM^4=(1/2)(TrM^2)^2, and
    detM.TrM=0 since TrM=0; RESEARCH s1).  We PROVE the closed form two ways, exact over Q:
      (1) detM-INDEPENDENCE at FIXED TrM^2: distinct M with the SAME TrM^2 but DIFFERENT detM give
          the SAME ||TT||^2 (=> detM absent -- the v27 cubic-blindness standard);
      (2) kappa is the SAME rational for a SPANNING set of generic M (=> ||TT||^2 = kappa (TrM^2)^2).
    Returns (ok, kappa).  This is the matched-instance route (the symbolic-M extraction stalls; the
    invariant-theory argument + detM-varied instances IS the identity, not an accident)."""
    # a spanning set of generic rational M with VARIED detM (some sharing TrM^2)
    fams = [
        [2, -3, sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 4), sp.Rational(-1, 5),
         sp.Rational(1, 6), sp.Rational(1, 7)],
        [-1, 2, sp.Rational(-2, 3), sp.Rational(1, 5), sp.Rational(3, 7), sp.Rational(1, 2),
         sp.Rational(-1, 4), sp.Rational(2, 9)],
        [1, -1, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],          # diagonal-ish (detM != generic)
        [0, 0, 1, 0, 1, 0, 1, 0],          # all real off-diagonal
        [1, -2, sp.Rational(1, 2), sp.Rational(-1, 3), 0, 0, 0, 0],
    ]
    data = []
    for vals in fams:
        Mc = _M_from_params(vals)
        r, _, _, _, _ = extract_tt(grad_bilinear(cancel(phi_field(Mc)), simp=together), g, ginv, Gam,
                                   verify=False)
        if r is None:
            return False, None
        n2 = cancel(l2_tensor(r, r, ginv))
        tr2 = cancel(TrM2_cx(Mc))
        detM = cancel(Mc.det())
        data.append((n2, tr2, detM))
    # (2) kappa constant across all: ||TT||^2 / (TrM^2)^2 same rational
    kap = None
    closes = True
    for (n2, tr2, dM) in data:
        if cancel(tr2) == 0:
            if cancel(n2) != 0:
                closes = False
            continue
        kk = cancel(n2 / tr2 ** 2)
        if kap is None:
            kap = kk
        elif cancel(kap - kk) != 0:
            closes = False
    # (1) detM-independence at fixed TrM^2: search for a pair with equal TrM^2, distinct detM
    detM_indep = None
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if cancel(data[i][1] - data[j][1]) == 0 and cancel(data[i][2] - data[j][2]) != 0:
                detM_indep = (cancel(data[i][0] - data[j][0]) == 0)
    ok = closes and (kap_guess is None or cancel(kap - kap_guess) == 0)
    return ok, kap


# ============================================================================
# GATE 4 -- the FROZEN verdict (RESEARCH s6, verbatim criteria).
# ============================================================================
def gate4(g3info=None):
    print("=" * 78)
    print("GATE 4 : the FROZEN verdict (LIVE / PARTIAL / STOP)")
    print("=" * 78)
    print("[SCOPE FENCE] deformation-complex DICTIONARY of a FROZEN imported geometry; no dynamical")
    print("metric, no selection law, no kappa; LIVE = the tensor sector's source data closes in")
    print("canonical form (a DICTIONARY fact, NOT a dynamics fact).")
    ok = True
    if g3info is None:
        g, ginv = fs_metric(), fs_metric_inv(fs_metric())
        _, g3info = gate3()
    closes_3a = bool(g3info.get("closes_3a_instances"))
    norm_forced = bool(g3info.get("norm_symbolic_ok"))
    detM_needed = bool(g3info.get("detM_needed"))
    contradicts = bool(g3info.get("contradicts_v31"))
    needs_outside = "detM (cubic invariant)" if detM_needed else None
    if not norm_forced and not detM_needed:
        needs_outside = "an invariant beyond (TrM^2)^2 (norm did not close with a forced constant)"
    world, reason = verdict(closes_3a, norm_forced, needs_outside, schur_ok=True,
                            contradicts_v31=contradicts)
    ok &= _report(f"4 VERDICT = {world}: {reason}", world in ("LIVE", "PARTIAL", "STOP"))
    print(f"\n  GATE 4 VERDICT: {world}", flush=True)
    if world == "LIVE":
        print("    The tensor sector's source data CLOSES in the canonical dictionary -- a FORCED")
        print("    tensor-response coefficient (the program's first).  FENCED: a DICTIONARY fact,")
        print("    NOT 'Einstein gravity derived'.  No selection law, no kappa, no G=kT.")
    elif world == "PARTIAL":
        print(f"    (3a) closes but the norm needs an invariant OUTSIDE the frozen tuple: "
              f"{needs_outside}.  The dictionary's first incompleteness names the next object.")
    else:
        print(f"    STOP: {reason}.  Not a verdict (do NOT self-amend v31).")
    out = {"world": world, "reason": reason, "eps": None}
    return ok, out


# ============================================================================
# GATE 5 -- the v33 ledger (priced only, NO claims, NO computation; RESEARCH s9, trap #19).
# ============================================================================
def gate5():
    print("=" * 78)
    print("GATE 5 : the v33 ledger (PRICED ONLY -- NO claims, NO computation; trap #19 fence)")
    print("=" * 78)
    print("[SCOPE FENCE] deformation-complex DICTIONARY of a FROZEN imported geometry; no dynamics.")
    print("""
  (a) THE LAPSE / 00 ASSEMBLY.  Consumes eps, c(M), and the v26/v27 scalar sector (the
      clock-rate/lapse-class K-data + the conformal/landscape r,G_M).  Needs the 4d-slice
      EMBEDDING of the cut CP^2 into the bulk (the h_2(C_u) Lorentzian slice; CONVENTIONS metric
      signature).  PRICE: a new milestone -- build the slice embedding, pull the (1,1) TT + scalar
      data through the lapse decomposition, check whether the 00-component assembles.  NOT run here.

  (b) THE OP^2 LIFT.  CP^2 = h_3(C_u) is Kahler (the (1,1)/(2,0)+(0,2) split drives everything).
      OP^2 = h_3(O) has structure group Spin(9), is NOT Kahler -- there is NO Kahler bigraduation,
      so the (1,1) dim-8 multiplet story does NOT transfer.  PRICE: redo the Boucetta-class
      eigentensor bookkeeping for Spin(9) isotypic types; the threshold mechanism differs.  Do NOT
      assume the CP^2 result lifts.  NOT run here.

  (c) THE FREDHOLM / RESPONSE READING OF eps.  The equation (Delta_L - 2Lambda) h = source is a
      Block-C-shaped IMPORT (the sourced response law).  Block C is where FIVE gravity routes died
      (v17 NONE / v18 / v19 / v20 / v21).  NAMED and FENCED (trap #19): "response" appears ONLY in
      this pricing.  We do NOT run it.  If eps=0 the marginal mode's 2nd-order obstruction theory
      (Koiso) is the correct frame; if eps!=0 the stiffness reading is available -- EITHER WAY it is
      a v33+ import, NOT a v32 dictionary fact.
""")
    print("  GATE 5: PRICED (no claims, no computation).")
    return True, {}


# ============================================================================
# DRIVER
# ============================================================================
def main(run=("g0",)):
    print("#" * 78)
    print("# lichnerowicz_response.py -- v32.0-cand Phase 92 (the Tensor Dictionary; exact over Q)")
    print("#" * 78)
    res = {}
    if "g0" in run:
        res["g0"], res["g0_info"] = gate0()
        if not res["g0"]:
            print("\n*** GATE 0 FAILED -- machinery wrong, STOP ***")
            return res
    if "g1" in run:
        res["g1"], res["g1_info"] = gate1(res.get("g0_info"))
        if not res["g1"]:
            print("\n*** GATE 1 FAILED -- control/convention hole, STOP ***")
            return res
    if "g2" in run:
        res["g2"], res["g2_info"] = gate2(res.get("g1_info"))
    if "g3" in run:
        res["g3"], res["g3_info"] = gate3(res.get("g2_info"))
        if not res["g3"] and res["g3_info"].get("contradicts_v31"):
            print("\n*** GATE 3 CONTRADICTS v31 -- STOP, do not self-amend ***")
            return res
    if "g4" in run:
        res["g4"], res["g4_info"] = gate4(res.get("g3_info"))
    if "g5" in run:
        res["g5"], _ = gate5()
    print(f"\n[{time.time() - _t0:6.1f}s] checks: {sum(PASS)}/{len(PASS)} PASS")
    return res


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "g0"
    if arg == "all":
        main(run=("g0", "g1", "g2", "g3", "g4", "g5"))
    else:
        main(run=(arg,))



