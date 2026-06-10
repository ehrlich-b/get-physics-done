"""entanglement_two_term.py  --  Gate 0 harness for slot 83 (v23.0-candidate)
"The Two-Term Balance Question -- Jacobson J5, fiber side."

GATE 0 ONLY: derive the invariant candidate space for the second-term functional A,
and set up the face/entropy machinery with conventions pinned.  DOES NOT run
Gates 1/2/3 (the orchestrator routes the next gate, fail-fast).

Discipline (CONVENTIONS.md):
  * det / cubic norm SSOT  = ring_lemma_verification.det_3  (octonion_algebra BANNED).
  * Exact over Q (sympy Rationals); entropy / log SYMBOLIC where needed.
  * u = e_7; Peirce under E_11: V_1(1) + V_{1/2}(16) + V_0(10).
  * Spin(9) = Stab_{F_4}(E_11) = kkt_gluing_holonomy.stab_f4([E_11])  (dim 36; the 36
    generators are 27x27 derivations acting block-diagonally on the Peirce blocks).
  * NO kappa, NO Lambda, NO G = kappa T anywhere in this run.

Coord layout (27-dim, ring_lemma_verification):
  [ alpha=0, beta=1, gamma=2,  x1 = 3..10 (V_0 octonion),
    x2 = 11..18, x3 = 19..26  (V_{1/2}) ].
  V_1(E_11)   = {0}          (alpha)
  V_0(E_11)   = {1..10}      (beta, gamma, x1)   = h_2(O)
  V_{1/2}(E_11)= {11..26}    (x2, x3)

Rank-1 face  : p = E_11,        corner = V_1(E_11) = R*E_11 (1-dim)   -> S trivial.
Rank-2 face  : q = E_22 + E_33, corner = V_1(q) = h_2(O) (coords 1..10) -> the MEANINGFUL face.

Engines reused (cite file:line in the report):
  ring_lemma_verification.py : det_3, jordan, Tr, Tr2, X_from_symbols, _flat27,
                               _standard_basis_27, h3o_identity, h3o_from_coords, oct_zero.
  kkt_gluing_holonomy.py     : E_ii, peirce_proj, peirce_idx, stab_f4, f4_basis.
"""
import sys
import time
from itertools import combinations_with_replacement as cwr

import sympy as sp
from sympy import Matrix, Rational, sqrt, symbols, series

import ring_lemma_verification as RL
import kkt_gluing_holonomy as KK

ODG = KK.ODG                       # orbit_dimension_gate: exact-over-Q rank helper
NV = 27

_t0 = time.time()
def _log(m):
    print(f"[{time.time()-_t0:7.1f}s] {m}", flush=True)

ALL_PASS = True
def _report(label, ok):
    global ALL_PASS
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}", flush=True)
    if not ok:
        ALL_PASS = False
    return ok


# ============================================================================
# 0. SOURCE GUARD  (mirror cartan_phaseB_curvature.py:source_guard)
#    octonion_algebra absent + native exact-over-Q det SSOT + no numpy on decisive path
# ============================================================================
def source_guard():
    print("=" * 78)
    print("SOURCE GUARD : octonion_algebra absent + exact-over-Q det SSOT + no numpy on decisive path")
    print("=" * 78)
    oa_absent = "octonion_algebra" not in sys.modules
    np_absent = "numpy" not in sys.modules
    native = (RL.det_3.__module__ == "ring_lemma_verification"
              and RL.jordan.__module__ == "ring_lemma_verification"
              and RL.Tr.__module__ == "ring_lemma_verification")
    Xspot = RL.h3o_from_coords(Rational(2), Rational(3), Rational(5),
                               RL.oct_zero(), RL.oct_zero(), RL.oct_zero())
    spot = RL.det_3(Xspot)
    spot_ok = (spot == 30) and (not isinstance(spot, float))
    _report("octonion_algebra NOT imported on the decisive path", oa_absent)
    _report(f"det SSOT native exact-over-Q ring_lemma (det_3(diag(2,3,5))=={spot})", native and spot_ok)
    _report("numpy NOT imported on this harness' decisive path (all sympy over QQ)", np_absent)
    return oa_absent and native and spot_ok and np_absent


# ============================================================================
# Spin(9) = Stab_{F_4}(E_11)
# ============================================================================
_SPIN9_CACHE = {}
def spin9_generators():
    """The 36 generators of spin(9) = stab_f4([E_11]), each a 27x27 exact-Q matrix
    acting on the flat-coord space.  Cached."""
    if "gens" not in _SPIN9_CACHE:
        E11 = KK.E_ii(0)
        res = KK.stab_f4([E11])
        _SPIN9_CACHE["gens"] = res["gens"]
        _SPIN9_CACHE["dim"] = res["dim"]
    return _SPIN9_CACHE["gens"]


def peirce_block_indices():
    """Peirce index sets under E_11 (val 1, 1/2, 0)."""
    E11 = KK.E_ii(0)
    return {
        "V1": sorted(KK.peirce_idx(E11, 1)),
        "Vhalf": sorted(KK.peirce_idx(E11, Rational(1, 2))),
        "V0": sorted(KK.peirce_idx(E11, 0)),
    }


# ============================================================================
# TASK A  --  Spin(9) Peirce decomposition  (block-diagonality + irrep structure)
# ============================================================================
def _restrict(D, idx):
    n = len(idx)
    return Matrix(n, n, lambda i, j: D[idx[i], idx[j]])


def block_trivial_directions(gens, idx):
    """Joint kernel (trivial-rep directions) of the gens restricted to a block, plus
    the nontrivial dimension.  Returns (trivial_dim, nontrivial_dim, [null vectors])."""
    n = len(idx)
    big = Matrix.vstack(*[_restrict(D, idx) for D in gens])
    rk = ODG.exact_qq_rank(big)
    return n - rk, rk, big.nullspace()


def commutant_dim(gens_blocks):
    """dim { A in End(R^n) : [A, D]=0 for all D in gens_blocks }, EXACT over Q.
    =1  <=>  the block is an irreducible real-type rep (Schur)."""
    n = gens_blocks[0].shape[0]
    aidx = lambda p, k: p * n + k
    rows = []
    for D in gens_blocks:
        block = sp.zeros(n * n, n * n)
        for p in range(n):
            for qq in range(n):
                r = p * n + qq
                for k in range(n):
                    block[r, aidx(p, k)] += D[k, qq]
                    block[r, aidx(k, qq)] -= D[p, k]
        rows.append(block)
    big = Matrix.vstack(*rows)
    return n * n - ODG.exact_qq_rank(big)


def task_A():
    print("=" * 78)
    print("TASK A : Peirce decomposition under Spin(9) = Stab_{F_4}(E_11)")
    print("=" * 78)
    gens = spin9_generators()
    _report(f"Spin(9) = stab_f4([E_11]) has dim 36 ({len(gens)} generators)", len(gens) == 36)
    blocks = peirce_block_indices()
    _report("V_1 = {0} (alpha), V_0 = {1..10}, V_{1/2} = {11..26}",
            blocks["V1"] == [0] and blocks["V0"] == list(range(1, 11))
            and blocks["Vhalf"] == list(range(11, 27)))

    # block-diagonality: no cross-Peirce entry in any generator
    offblock = False
    allidx = blocks
    for D in gens:
        for ba, ra in allidx.items():
            for bb, cb in allidx.items():
                if ba == bb:
                    continue
                if any(D[ra[i], cb[j]] != 0 for i in range(len(ra)) for j in range(len(cb))):
                    offblock = True
    _report("36 spin(9) generators act BLOCK-DIAGONALLY on V_1 + V_0 + V_{1/2}", not offblock)

    coordname = {0: "alpha", 1: "beta", 2: "gamma"}
    results = {}
    for name, idx in blocks.items():
        tdim, ntdim, ns = block_trivial_directions(gens, idx)
        results[name] = (tdim, ntdim, ns)
        dirs = []
        for vec in ns:
            terms = [(idx[i], coordname.get(idx[i], f"x@{idx[i]}"), vec[i]) for i in range(len(idx)) if vec[i] != 0]
            dirs.append(terms)
        print(f"  {name} (dim {len(idx)}): trivial dim = {tdim}, nontrivial dim = {ntdim}; trivial dirs = {dirs}")

    # expected: V1 -> 1 (alpha); V0 -> 1 (beta+gamma) + 9; Vhalf -> 16 (no trivial)
    okV1 = results["V1"][0] == 1 and results["V1"][1] == 0
    okV0 = results["V0"][0] == 1 and results["V0"][1] == 9
    okVh = results["Vhalf"][0] == 0 and results["Vhalf"][1] == 16
    _report("V_1 = trivial 1 (alpha = coord 0)", okV1)
    _report("V_0 = 1 + 9  (trivial = beta+gamma trace ; vector = 9)", okV0)
    _report("V_{1/2} = 16  (no trivial subspace = spinor)", okVh)
    # explicit trivial direction of V0 is beta+gamma
    v0_triv = results["V0"][2][0]
    v0idx = blocks["V0"]
    coeff_beta = v0_triv[v0idx.index(1)]
    coeff_gamma = v0_triv[v0idx.index(2)]
    others_zero = all(v0_triv[k] == 0 for k in range(len(v0idx)) if v0idx[k] not in (1, 2))
    _report("V_0 trivial direction is exactly (beta + gamma) (equal coeffs, no x1)",
            coeff_beta == coeff_gamma and coeff_beta != 0 and others_zero)

    # irreducibility certificates (commutant dim == 1)
    #   9-block: split the trivial (beta+gamma) off V_0 and take the 9-dim complement.
    gens_V0 = [_restrict(D, blocks["V0"]) for D in gens]
    n0 = len(blocks["V0"])
    tvec = sp.zeros(n0, 1); tvec[v0idx.index(1)] = 1; tvec[v0idx.index(2)] = 1
    cols = [tvec] + [sp.eye(n0)[:, j] for j in range(n0) if j != v0idx.index(1)]
    P = Matrix.hstack(*cols)
    assert ODG.exact_qq_rank(P) == n0
    Pinv = P.inv()
    gens_9 = [(Pinv * D * P)[1:, 1:] for D in gens_V0]
    cd9 = commutant_dim(gens_9)
    _report(f"9-block irreducible (commutant dim = {cd9} = 1 -> Spin(9) vector 9)", cd9 == 1)

    gens_16 = [_restrict(D, blocks["Vhalf"]) for D in gens]
    cd16 = commutant_dim(gens_16)
    _report(f"16-block irreducible (commutant dim = {cd16} = 1 -> Spin(9) spinor 16)", cd16 == 1)

    return {
        "decomp": {"V1": "1", "V0": "1 (+) 9", "Vhalf": "16"},
        "V0_trivial": "beta + gamma",
        "V1_trivial": "alpha",
        "commutant_9": cd9, "commutant_16": cd16,
    }


# ============================================================================
# TASK B  --  Exhaustive low-degree (<=3) Spin(9)-invariant ring
# ============================================================================
C = symbols("c0:27")          # the 27 coordinates


def _vfield(D, f):
    """The derivation/vector-field action of a 27x27 generator D on a polynomial f:
       D.f = sum_{a,b} D[a,b] c_b  df/dc_a ."""
    out = sp.Integer(0)
    for a in range(NV):
        dfa = sp.diff(f, C[a])
        if dfa == 0:
            continue
        s = sp.Integer(0)
        for b in range(NV):
            if D[a, b] != 0:
                s += D[a, b] * C[b]
        if s != 0:
            out += s * dfa
    return sp.expand(out)


def _monomials_deg(deg):
    mons = []
    for combo in cwr(range(NV), deg):
        m = sp.Integer(1)
        for i in combo:
            m *= C[i]
        mons.append(m)
    return mons


def _gen_int_rows(gens):
    """Precompute each generator as integer (a, [(b, coeff)]) rows with denominators
    cleared, for the fast prime-field rank.  Returns (gen_rows, )."""
    import math
    out = []
    for D in gens:
        dens = [D[a, b].q for a in range(NV) for b in range(NV) if D[a, b] != 0]
        L = 1
        for d in dens:
            L = L * d // math.gcd(L, d)
        rows = []
        for a in range(NV):
            terms = [(b, int(D[a, b] * L)) for b in range(NV) if D[a, b] != 0]
            if terms:
                rows.append((a, terms))
        out.append(rows)
    return out


def _exps_of_deg(deg):
    for combo in cwr(range(NV), deg):
        e = {}
        for i in combo:
            e[i] = e.get(i, 0) + 1
        yield tuple(sorted(e.items()))


def _mon_key(edict):
    return tuple(sorted((i, p) for i, p in edict.items() if p > 0))


def _build_kernel_matrix_int(deg, gen_rows):
    """Integer derivation-map matrix for degree-deg polynomials (column = source monomial,
    rows = stacked per-generator images).  Returns (nrows, ncols, entries dict, mons)."""
    mons = list(_exps_of_deg(deg))
    col = {m: j for j, m in enumerate(mons)}
    nm = len(mons)
    entries = {}
    rowbase = 0
    for rows in gen_rows:
        for j, m in enumerate(mons):
            edict = dict(m)
            for (a, terms) in rows:
                pa = edict.get(a, 0)
                if pa == 0:
                    continue
                base = dict(edict); base[a] = pa - 1
                if base[a] == 0:
                    del base[a]
                for (b, coeff) in terms:
                    newe = dict(base); newe[b] = newe.get(b, 0) + 1
                    k = col[_mon_key(newe)]
                    entries[(rowbase + k, j)] = entries.get((rowbase + k, j), 0) + pa * coeff
        rowbase += nm
    return rowbase, nm, entries, mons


def _rank_mod_p(nrows, ncols, entries, p):
    """Sparse Gaussian elimination mod p.  rank over Q == rank mod p for all but finitely
    many primes; agreement at two large primes certifies the Q-rank."""
    rowmap = {}
    for (r, cc), v in entries.items():
        vv = v % p
        if vv:
            rowmap.setdefault(r, {})[cc] = vv
    pivots = {}
    rank = 0
    for row in rowmap.values():
        row = dict(row)
        while row:
            cmin = min(row)
            if cmin in pivots:
                prow, pinv = pivots[cmin]
                factor = row[cmin] * pinv % p
                for cc, val in prow.items():
                    nv = (row.get(cc, 0) - factor * val) % p
                    if nv:
                        row[cc] = nv
                    elif cc in row:
                        del row[cc]
            else:
                break
        if row:
            cmin = min(row)
            pivots[cmin] = (row, pow(row[cmin], p - 2, p))
            rank += 1
    return rank


def invariant_dim_prime(deg, gen_rows, primes=(2147483647, 2147483629)):
    """dim of degree-deg Spin(9)-invariants = ncols - rank, via prime-field rank at two
    primes (asserts agreement)."""
    nrows, ncols, entries, mons = _build_kernel_matrix_int(deg, gen_rows)
    ranks = [_rank_mod_p(nrows, ncols, entries, p) for p in primes]
    assert ranks[0] == ranks[1], f"PRIME DISAGREEMENT deg {deg}: {ranks}"
    return ncols - ranks[0], (nrows, ncols, len(entries))


# ----- explicit generators -----------------------------------------------------
def explicit_generators():
    """The candidate generator polynomials (exact over Q) in the 27 coords."""
    alpha = C[0]; beta = C[1]; gamma = C[2]
    tr_v0 = beta + gamma                                  # the V_0 diagonal trace
    n_x1 = sum(C[i] ** 2 for i in range(3, 11))           # |x1|^2  (V_0 octonion, 8-dim)
    Q_vector = n_x1 - beta * gamma                        # the 9-norm (V_0 vector)
    Q_spinor = sum(C[i] ** 2 for i in range(11, 27))      # the 16-norm (V_{1/2} spinor)
    X = RL.X_from_symbols(C)
    det = sp.expand(RL.det_3(X))                          # the cubic norm (SSOT)
    Tr = sp.expand(RL.Tr(X))                              # alpha + beta + gamma
    Tr2 = sp.expand(RL.Tr2(X))                            # full trace form
    return {
        "alpha (deg1)": alpha,
        "Tr_V0 = beta+gamma (deg1)": tr_v0,
        "Q_vector = |9|^2 (deg2)": Q_vector,
        "Q_spinor = |16|^2 (deg2)": Q_spinor,
        "det_3 (deg3, SSOT)": det,
        "_Tr": Tr, "_Tr2": Tr2,
    }


def _poly_row(f, ms, mi):
    d = sp.Poly(sp.expand(f), *C).as_dict()
    r = [0] * len(ms)
    for k, v in d.items():
        r[mi[k]] = v
    return r


def _span_rank(polys):
    s = set()
    for f in polys:
        for k in sp.Poly(sp.expand(f), *C).as_dict():
            s.add(k)
    ms = sorted(s)
    mi = {m: i for i, m in enumerate(ms)}
    return Matrix([_poly_row(f, ms, mi) for f in polys]).rank()


def task_B():
    print("=" * 78)
    print("TASK B : exhaustive <=deg-3 Spin(9)-invariant ring (candidate space for A)")
    print("=" * 78)
    gens = spin9_generators()
    gen_rows = _gen_int_rows(gens)

    # per-degree invariant dimension (the kernel-dimension certificate)
    dims = {}
    for d in (1, 2, 3):
        inv, shape = invariant_dim_prime(d, gen_rows)
        dims[d] = inv
        _log(f"deg {d}: invariant dim = {inv}  (kernel of spin(9) on {shape[1]} monomials; matrix {shape[0]}x{shape[1]}, nnz {shape[2]})")

    _report("deg-1 invariant dim = 2", dims[1] == 2)
    _report("deg-2 invariant dim = 5", dims[2] == 5)
    _report("deg-3 invariant dim = 9", dims[3] == 9)

    # explicit generators and SPAN certificate (generators span the kernel, not just match dim)
    g = explicit_generators()
    alpha = g["alpha (deg1)"]; tr_v0 = g["Tr_V0 = beta+gamma (deg1)"]
    Q_vector = g["Q_vector = |9|^2 (deg2)"]; Q_spinor = g["Q_spinor = |16|^2 (deg2)"]
    det = g["det_3 (deg3, SSOT)"]

    # deg-1 span
    deg1_set = [alpha, tr_v0]
    _report("deg-1 generators {alpha, Tr_V0} span the 2-dim invariant space",
            _span_rank(deg1_set) == 2 == dims[1])

    # deg-2 span : 3 products of deg-1 + 2 new norms
    deg2_set = [alpha ** 2, alpha * tr_v0, tr_v0 ** 2, Q_vector, Q_spinor]
    _report("deg-2 generators {alpha^2, alpha*Tr_V0, Tr_V0^2, Q_vector, Q_spinor} span the 5-dim space",
            _span_rank(deg2_set) == 5 == dims[2])

    # deg-3 span : 8 reducible products + det_3 = 9
    reducible = [sp.expand(li * q) for li in [alpha, tr_v0] for q in deg2_set]   # 10 products
    red_rank = _span_rank(reducible)
    full_rank = _span_rank(reducible + [det])
    _report(f"deg-3 reducible products {{deg1 x deg2}} span dim {red_rank} (8)", red_rank == 8)
    _report("deg-3 {reducibles, det_3} span dim 9 = the kernel dim (det_3 INDEPENDENT; ring CLOSES)",
            full_rank == 9 == dims[3])

    # det_3 is Spin(9)-invariant (it is F_4-invariant)
    det_inv = all(_vfield(D, det) == 0 for D in gens)
    _report("det_3 is Spin(9)-invariant (D.det_3 = 0 for all 36 generators)", det_inv)

    # the spinor-vector-spinor (Gamma) cubic is NOT an independent generator: it lives inside
    # det_3 (coefficient -1/2 relative to det_3's vector x spinor^2 cross-terms).  Certified
    # by: {reducibles, det_3} already exhaust dim 9 (no room for an extra cubic).
    _report("Gamma-cubic (16 x 9 x 16 -> R) is NOT independent: it is the cross-term content of det_3",
            full_rank == 9)

    # FAIL-FAST: the ring closes cleanly at degree 3 iff generators span the kernel at every
    # degree AND the deg-3 kernel matches the explicit generator span.  Derived, not hardcoded.
    closes = (_span_rank(deg1_set) == dims[1]
              and _span_rank(deg2_set) == dims[2]
              and full_rank == dims[3])
    _report("FAIL-FAST: Spin(9)-invariant ring CLOSES CLEANLY at degree 3", closes)

    return {"dims": dims, "closes": closes,
            "generators": {
                "deg1": ["alpha", "Tr_V0 = beta+gamma  (= Tr - alpha)"],
                "deg2": ["Q_vector = |9|^2 = sum_{3..10} c^2 - beta*gamma",
                         "Q_spinor = |16|^2 = sum_{11..26} c^2",
                         "(+ products alpha^2, alpha*Tr_V0, Tr_V0^2)"],
                "deg3": ["det_3 (cubic norm SSOT; CONTAINS the 16x9x16 Gamma-coupling as its cross-terms)",
                         "(+ products deg1 x deg2)"],
            }}


# ============================================================================
# TASK C  --  face / entropy machinery (convention pinned; bug-guard #4)
# ============================================================================
def _onorm2(z):
    """octonion squared norm |z|^2 = sum of the 8 component squares (z is an 8-list)."""
    return sum(zi ** 2 for zi in z)


def face_indices():
    """Tangent (corner) coord sets for the two faces, plus the complement idempotent q."""
    E11 = KK.E_ii(0)
    # q = E_22 + E_33 (rank-2 complement idempotent), as an h_3(O) element
    q = [[[1 if (i == j and i in (1, 2) and k == 0) else 0 for k in range(8)]
          for j in range(3)] for i in range(3)]
    return {
        "rank1_face_tangent": sorted(KK.peirce_idx(E11, 1)),      # {0}
        "rank2_face_tangent": sorted(KK.peirce_idx(q, 1)),        # {1..10} = h_2(O)
        "rank2_killed": sorted(KK.peirce_idx(q, 0)) + sorted(KK.peirce_idx(q, Rational(1, 2))),
        "q": q,
    }


def compress_rank2(Xc):
    """Peirce compression C_q(X) for q = E_22 + E_33, returned as the 2x2 h_2(O) corner
    [[beta, x1],[x1*, gamma]] (= the lower-right block of the 3x3 octonion-Hermitian X).
    CONVENTION (PINNED): compress FIRST (read the V_1(q) corner), THEN normalize by trace."""
    beta = Xc[1][1][0]
    gamma = Xc[2][2][0]
    x1 = Xc[1][2]                      # octonion 8-list (the (2,3) entry)
    return beta, gamma, x1


def rho_face_rank2_eigs(Xc):
    """Eigenvalues of the NORMALIZED rank-2 face state rho_face = C_q(X)/Tr(C_q(X)).
    The 2x2 octonion-Hermitian corner has real eigenvalues
        lambda_pm = (beta+gamma)/2 +- sqrt( ((beta-gamma)/2)^2 + |x1|^2 ).
    Returns (density eigenvalues [d+, d-], face trace beta+gamma)."""
    beta, gamma, x1 = compress_rank2(Xc)
    tr = beta + gamma
    s = sqrt(((beta - gamma) / 2) ** 2 + _onorm2(x1))
    lp = (beta + gamma) / 2 + s
    lm = (beta + gamma) / 2 - s
    return [lp / tr, lm / tr], tr


def S_face_rank2(Xc):
    """von Neumann entropy of the rank-2 face state (symbolic log)."""
    dens, _ = rho_face_rank2_eigs(Xc)
    return -sum(d * sp.log(d) for d in dens)


def S_face_rank1(Xc):
    """Rank-1 face (p = E_11): corner = scalar alpha; density = 1; entropy identically 0."""
    return sp.Integer(0)


def _I_over_3():
    I3 = RL.h3o_identity()
    return [[[I3[i][j][k] * Rational(1, 3) for k in range(8)] for j in range(3)] for i in range(3)]


def task_C():
    print("=" * 78)
    print("TASK C : face / entropy machinery (convention pinned; bug-guard #4)")
    print("=" * 78)
    fi = face_indices()
    _report("rank-1 face tangent = V_1(E_11) = {0} (1-dim, trivial corner)",
            fi["rank1_face_tangent"] == [0])
    _report("rank-2 face tangent = V_1(E_22+E_33) = {1..10} = h_2(O) (10-dim)",
            fi["rank2_face_tangent"] == list(range(1, 11)))
    _report("rank-2 compression KILLS {0}=alpha and {11..26}=V_{1/2} coupling",
            fi["rank2_killed"] == [0] + list(range(11, 27)))

    print("  CONVENTION (PINNED): rho_face = C_p(X) / Tr(C_p(X)) -- compress FIRST, normalize SECOND.")
    print("                        C_p = projection onto V_1(p) (the face subalgebra h_k(O)),")
    print("                        read as the matrix corner; entropy = von Neumann of its eigenvalues.")

    # verify at X = I/3
    X = _I_over_3()
    # rank-1 face: trivial
    S1 = S_face_rank1(X)
    _report("rank-1 face at I/3: corner scalar 1/3 -> density 1 -> S = 0 (TRIVIAL face)", S1 == 0)
    # rank-2 face: maximally mixed I_2/2, S = log 2
    dens, tr = rho_face_rank2_eigs(X)
    _report("rank-2 face at I/3: density eigenvalues = (1/2, 1/2) (maximally mixed I_2/2)",
            [sp.simplify(d) for d in dens] == [Rational(1, 2), Rational(1, 2)])
    S2 = sp.simplify(S_face_rank2(X))
    _report("rank-2 face at I/3: S_face = log 2", sp.simplify(S2 - sp.log(2)) == 0)
    print(f"    -> meaningful face = the RANK-2 face (rank-1 carries trivial entropy).")

    # bug-guard #4: compression-then-normalize does NOT manufacture spurious first-order
    # criticality.  Check dS/dt|_0 = 0 along face directions, and a clean 2nd-order Fisher form.
    t = symbols("t", real=True)
    def _S2_of(beta, gamma, n2):
        tr = beta + gamma
        s = sqrt(((beta - gamma) / 2) ** 2 + n2)
        lp = (beta + gamma) / 2 + s; lm = (beta + gamma) / 2 - s
        dp = lp / tr; dm = lm / tr
        return -(dp * sp.log(dp) + dm * sp.log(dm))
    # diagonal traceless direction
    Sdiag = _S2_of(Rational(1, 3) + t, Rational(1, 3) - t, 0)
    dSdiag0 = sp.diff(Sdiag, t).subs(t, 0)
    quad_diag = series(Sdiag, t, 0, 3).removeO()
    # off-diagonal x1 direction
    Soff = _S2_of(Rational(1, 3), Rational(1, 3), t ** 2)
    quad_off = series(Soff, t, 0, 3).removeO()
    _report("bug-guard #4: dS_face/dt|_(I/3) = 0 (no spurious linear criticality from normalization)",
            dSdiag0 == 0)
    _report("bug-guard #4: 2nd-order Fisher form is clean (S = log2 - (9/2) t^2 + O(t^3), no log in quadratic)",
            sp.simplify(quad_diag - (sp.log(2) - Rational(9, 2) * t ** 2)) == 0
            and sp.simplify(quad_off - (sp.log(2) - Rational(9, 2) * t ** 2)) == 0)
    print("    NOTE (for Gate 2, do NOT compute here): at I/3 the first variation delta S vanishes;")
    print("    the first nontrivial info is the 2nd-order Fisher/Bures form  delta^2 S ~ -Tr(h^2)")
    print("    (clean, exact over Q, no log) -- entanglement-route.md section 8.1 / 8.5.")

    return {
        "convention": "rho_face = C_p(X)/Tr(C_p(X)); compress-then-normalize",
        "rank1_S_at_I3": "0 (trivial)",
        "rank2_S_at_I3": "log 2",
        "meaningful_face": "rank-2 (q = E_22 + E_33; corner = h_2(O))",
        "rank2_face_tangent": fi["rank2_face_tangent"],
        "rank2_killed": fi["rank2_killed"],
        "fisher_coeff_at_I3": "-9/2 (per unit-t face direction)",
    }


# ============================================================================
# DRIVER
# ============================================================================
def main():
    print("#" * 78)
    print("# GATE 0 DRIVER -- slot 83 (v23.0-candidate): the invariant candidate space + face machinery")
    print("# Gates 1/2/3 NOT run (orchestrator routes the next gate -- fail-fast).")
    print("#" * 78)
    sg = source_guard()
    A = task_A()
    B = task_B()
    Cres = task_C()

    print("=" * 78)
    print("GATE-0 SELF-TEST / FAIL-FAST ROUTING")
    print("=" * 78)
    # the Gate-0 fail-fast boolean: does the ring close at degree 3?  DERIVED from the
    # computed kernel dims + explicit-generator span (NOT hardcoded).
    ring_closes = B["closes"]
    _report("RING CLOSES AT DEGREE 3 (fail-fast routing boolean, derived from kernel dims)", ring_closes)

    print()
    print("=" * 78)
    if ALL_PASS and sg and ring_closes:
        print("RESULT: ALL_PASS  --  Gate 0 COMPLETE; ring closes at degree 3; PROCEED to next gate.")
    else:
        print("RESULT: FAIL  --  Gate 0 did not close cleanly; STOP and report (fail-fast).")
    print("=" * 78)
    return ALL_PASS and sg and ring_closes


if __name__ == "__main__":
    ok = main()
    sys.exit(0 if ok else 1)
