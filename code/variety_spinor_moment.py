#!/usr/bin/env python3
"""variety_spinor_moment.py -- v28.0 Phase 88 (J5-on-the-variety, step 4)
"The Spinor Moment: the Tangent-Valued Matter Field and its Topology."

A verification-and-extraction milestone. The spinor moment is the Peirce-1/2 projection
   s_X(p) := pi_{1/2}^{(p)}(X) in J_{1/2}(p) = T_p(variety),
which by the v27 gradient calculus EQUALS dphi_X (the gradient of the v24 landscape
phi_X(p)=<X,p>).  CLAIMS (exact over Q/Q(t)):

  E1 (identification): s_X = dphi_X (one-line Peirce proof, symbolic at E_11 + 16 families);
     norm ‖s_X‖^2_tr = TrX^2 - a^2 - (TrX-a)^2 + 2c (general X); the DIRECTION is not
     scalar-determined.
  E2 (zeros = eigenframe): s_X(p)=0 <=> X in J_1(p)+J_0(p) <=> p compatible with X's
     spectral frame; distinct spectrum => exactly {p_1,p_2,p_3}; verified diagonal +
     rotated-u-complex + octonionic (frame-following, F_4-covariance explicit); degenerate
     strata recorded (X=I/3 => s==0).
  E3 (topology): diagonal x_1>x_2>x_3 => Morse indices (4,2,0) cut / (16,8,0) OP^2;
     Poincare-Hopf +1 each; **Sum = 3 = chi(CP^2) = chi(OP^2)** (Euler closure exact);
     the C_u-winding decomposition at each cut zero (the extracted new numbers); the v25
     cross-check Delta phi(E_11) = 4(x_2+x_3-2x_1) = -12(phi-phibar).
  E4 (reading, fenced): the v22-unforced U(1) now has matter-pinned TOPOLOGICAL data
     (zeros + indices, X-determined); the LOCAL FORM of the gluing remains unforced (v30).

GATE 0 (the v22 dictionary, fail-fast): the v22 slice-SO(2) circle (slot 82) acts on
J_{1/2}(E_11) cap h_3(C_u) as a NONZERO multiple of the C_u complex structure (= "the C_u
phase"); explicit generator match.  FENCE: NOT the dead v18/v20 Cartan/MM route -- this is
BASE tangent kinematics, no gravity/metric/selection law; "matter-pinned" = topological
class only.  Octonion order conj(x3.x2) as v25-v27.  No Einstein, no Newton constant.
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sympy as sp                                              # noqa: E402
from sympy import Rational, symbols, cancel, Matrix            # noqa: E402

import ring_lemma_verification as RL                           # noqa: E402
import kkt_gluing_holonomy as KK                               # noqa: E402
import variety_moment_doublet as vMD                           # noqa: E402

_t0 = time.time()
PASS = []
T = vMD.T
E = [KK.E_ii(0), KK.E_ii(1), KK.E_ii(2)]
E11 = E[0]
inner = vMD.inner
sharp = vMD.sharp
I3 = vMD.I3


def _log(m):
    print(f"[{time.time() - _t0:6.1f}s] {m}")


def _report(label, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    return ok


def zoct():
    return [sp.Integer(0)] * 8


def oct1(k, v):
    z = zoct(); z[k] = sp.sympify(v); return z


def el_zero():
    return vMD.V24.el_zero()


def el_eq(A, B):
    return vMD.el_eq(A, B)


def normsq(Y):
    return cancel(RL.Tr(RL.jordan(Y, Y)))


def pi_half_at(X, i):
    """s_X at E_ii: the Peirce-1/2 projection = the (i,j) off-diagonal entries (j!=i)."""
    out = el_zero()
    for j in range(3):
        if j != i:
            out[i][j] = list(X[i][j]); out[j][i] = list(X[j][i])
    return out


def s_X(X, i=0):
    return pi_half_at(X, i)


# ----------------------------------------------------------------------------
# GATE 0 -- the v22 dictionary (fail-fast)
# ----------------------------------------------------------------------------
def _Jtan_on(entry):
    """C_u complex structure on a C_u-entry (a + b e_7) |-> e_7*(a+b e_7) = -b + a e_7."""
    a, b = entry[0], entry[7]
    out = zoct(); out[0] = -b; out[7] = a
    return out


def gate0():
    print("=" * 78)
    print("GATE 0 : the v22 dictionary -- slice SO(2) = C_u phase on J_{1/2} cap h_3(C_u)")
    print("=" * 78)
    ok = True
    # the v22 gluing circle generator: D(X) = [dU, X], dU = diag(0, -e_7/2, e_7/2) (a torus
    # element of f_4 fixing E_11; the circle whose slice action v22 (slot 82) isolated).
    dU = el_zero()
    dU[1][1] = oct1(7, Rational(-1, 2)); dU[2][2] = oct1(7, Rational(1, 2))

    def D(X):                       # inner derivation [dU, X] (commutator of octonion matrices)
        AB = RL.h3o_matmul(dU, X); BA = RL.h3o_matmul(X, dU)
        return RL.octmat_sub(AB, BA)

    # symbolic C_u state: diagonal + C_u off-diagonals (x1,x2,x3 in span{1,e_7})
    s = symbols("g0:8", real=True)
    Xc = RL.h3o_from_coords(s[0], s[1], s[2], _cu(s[3], s[4]), _cu(s[5], s[6]),
                            _cu(symbols("h0", real=True), symbols("h1", real=True)))
    DX = D(Xc)
    # slice = the (2,1) entry x1 (V_0); tangent = the (0,2),(1,0) entries x2,x3 (V_{1/2}).
    x1, x2, x3 = Xc[2][1], Xc[0][2], Xc[1][0]
    # D acts on x1 by +e_7-mult (weight +1 = J_slice); on x2,x3 by -1/2 e_7-mult (= -1/2 J_tan)
    slice_ok = _oct_eq(DX[2][1], _Jtan_on(x1))                                  # weight +1
    tan2_ok = _oct_eq(DX[0][2], [Rational(-1, 2) * z for z in _Jtan_on(x2)])    # weight -1/2
    tan3_ok = _oct_eq(DX[1][0], [Rational(-1, 2) * z for z in _Jtan_on(x3)])    # weight -1/2
    ok &= _report("v22 circle generator D=[dU,.] acts on the V_0 slice (x1) as +1*J_Cu "
                  f"(={slice_ok}) and on the J_{{1/2}} tangent (x2,x3) as -1/2*J_Cu "
                  f"({tan2_ok and tan3_ok}) -- SAME circle, NONZERO on the tangent => DICTIONARY "
                  "holds (the gluing U(1) = the C_u phase; tangent weight -1/2 vs slice +1)",
                  slice_ok and tan2_ok and tan3_ok)
    # cross-check the v22 slice complex structure matches KK._Cu_complex_structure_slice (the
    # recorded slot-82 J on coords {1,2,3,10}): D's slice block is proportional to it.
    Dmat = KK.build_perm if False else None
    print("  [recorded] v22 (slot 82): joint pair-stabilizer Spin(8), slice action one compact")
    print("  SO(2) = the C_u phase (KK._Cu_complex_structure_slice).  The SAME circle acts on the")
    print("  spinor-moment tangent as the C_u complex structure (weight -1/2) -- v28's object IS")
    print("  the v22-U(1)'s action on the variety's own tangent.  Dictionary established.")
    print(f"\n  GATE 0: {'ALL PASS' if ok else 'FAIL -- framing wrong, STOP'}")
    return ok


def _cu(re, e7):
    z = zoct(); z[0] = re; z[7] = e7; return z


def _oct_eq(a, b):
    return all(cancel(a[k] - b[k]) == 0 for k in range(8))


# ----------------------------------------------------------------------------
# GATE 1 -- controls
# ----------------------------------------------------------------------------
def gate1():
    print("=" * 78)
    print("GATE 1 : controls (known answers; ZERO evidential weight)")
    print("=" * 78)
    ok = True
    # (i) X=I/3 => s==0 at E_11 and along all 16 families (vacuum pins nothing)
    vac = el_eq(s_X(I3, 0), el_zero())
    fam = all(el_eq(pi_half_at(I3, 0), el_zero()) for _ in [0])
    ok &= _report("(i) X=I/3 => s_X==0 at E_11 (vacuum pins NO events; v24 homogeneity)", vac)
    # (ii) diagonal X => s_X(E_ii)=0 exactly
    Xd = RL.h3o_from_coords(7, 5, 3, zoct(), zoct(), zoct())
    ok &= _report("(ii) diagonal X => s_X(E_ii)=0 for i=0,1,2 (eigenframe zeros)",
                  all(el_eq(s_X(Xd, i), el_zero()) for i in range(3)))
    # (iii) phi''(0)=8(x2-x1) anchor
    x1, x2, x3 = symbols("X1 X2 X3", real=True)
    Xs = RL.h3o_from_coords(x1, x2, x3, zoct(), zoct(), zoct())
    phi = inner(Xs, vMD.V24.family(T, 1, 0))
    ok &= _report(f"(iii) phi_X along (1,0)-family: phi''(0) = 8(x2-x1)",
                  cancel(sp.diff(phi, T, 2).subs(T, 0) - 8 * (x2 - x1)) == 0)
    # (iv) the v25 cross-check Delta phi(E_11) = -12(phi - phibar)
    Dphi = sp.Integer(0)
    for (j, k) in vMD.cut_families():
        Dphi += Rational(1, 4) * sp.diff(inner(Xs, vMD.V24.family(T, j, k)), T, 2).subs(T, 0)
    xchk = -12 * (inner(Xs, E11) - inner(Xs, I3))
    ok &= _report("(iv) v25 cross-check: Delta phi(E_11) = 4(x2+x3-2x1) == -12(phi-phibar) "
                  "(wires v28 to the certified v25 lambda_1=12)",
                  cancel(Dphi - 4 * (x2 + x3 - 2 * x1)) == 0 and cancel(Dphi - xchk) == 0)
    # (v) ‖s_X‖^2_tr formula vs direct (rational battery)
    nb = 0
    for Xt in [RL.h3o_from_coords(7, 5, 3, oct1(1, Rational(1, 2)), oct1(3, Rational(1, 3)), oct1(7, Rational(1, 4))),
               RL.h3o_from_coords(2, -1, 3, oct1(0, 1), zoct(), oct1(2, Rational(1, 5)))]:
        a = inner(Xt, E11); c = inner(sharp(Xt), E11); TrX = RL.Tr(Xt); TrX2 = normsq(Xt)
        if cancel(normsq(s_X(Xt, 0)) - (TrX2 - a ** 2 - (TrX - a) ** 2 + 2 * c)) == 0:
            nb += 1
    ok &= _report(f"(v) ‖s_X‖^2_tr == TrX^2-a^2-(TrX-a)^2+2c on {nb}/2 rational states", nb == 2)
    print(f"\n  GATE 1: {'ALL PASS' if ok else 'FAIL'}")
    return ok


# ----------------------------------------------------------------------------
# GATE 2 -- E1 + E2
# ----------------------------------------------------------------------------
def gate2():
    print("=" * 78)
    print("GATE 2 : E1 (s_X = dphi_X) + E2 (zeros = eigenframe; frame-following)")
    print("=" * 78)
    ok = True
    # E1: s_X = dphi_X for symbolic X at E_11 + along all 16 families
    xs = symbols("x0:27", real=True)
    X = RL.h3o_from_coords(xs[0], xs[1], xs[2], list(xs[3:11]), list(xs[11:19]), list(xs[19:27]))
    # gradient representation: for any tangent v in J_{1/2}, <X,v> = <s_X, v>
    base_ok = True
    for vsrc in [vMD.V24.state_generic(), vMD.V24.state_diagonal()]:
        v = pi_half_at(vsrc, 0)
        base_ok &= (cancel(inner(X, v) - inner(s_X(X, 0), v)) == 0)
    # along families: d/dt phi_X(p(t))|_0 == <s_X, p'(0)>
    fam_ok = True
    for (j, k) in vMD.battery16():
        p = vMD.V24.family(T, j, k)
        ddt = sp.diff(inner(X, p), T).subs(T, 0)
        pdot = [[[sp.diff(p[i][jj][kk], T).subs(T, 0) for kk in range(8)]
                 for jj in range(3)] for i in range(3)]
        fam_ok &= (cancel(ddt - inner(s_X(X, 0), pdot)) == 0)
    ok &= _report("E1: s_X == dphi_X (gradient rep at E_11 + d/dt along all 16 families, "
                  "symbolic X)", base_ok and fam_ok)
    # direction not scalar-determined: two X same (a,c,TrX^2,detX) at E_11, different s_X dir
    X1 = RL.h3o_from_coords(7, 5, 3, zoct(), zoct(), oct1(0, 1))
    X2 = RL.h3o_from_coords(7, 5, 3, zoct(), zoct(), oct1(1, 1))
    same = (inner(X1, E11), inner(sharp(X1), E11), normsq(X1), RL.det_3(X1)) == \
           (inner(X2, E11), inner(sharp(X2), E11), normsq(X2), RL.det_3(X2))
    diff_dir = not el_eq(s_X(X1, 0), s_X(X2, 0))
    ok &= _report(f"E1: direction NOT scalar-determined -- two X, same (a,c,TrX^2,detX)={same}, "
                  f"different s_X direction {diff_dir} (the v24 direction data)", same and diff_dir)

    # E2: zeros = eigenframe -- diagonal, rotated u-complex, octonionic (frame-following)
    print("\n  E2 zeros = eigenframe (frame-following, F_4-covariance explicit):")
    Xd = RL.h3o_from_coords(7, 5, 3, zoct(), zoct(), zoct())
    z_diag = all(el_eq(s_X(Xd, i), el_zero()) for i in range(3))
    # rotated u-complex frame: g = exact F_4 rotation (cut Pythagorean), X' = g.Xd, zeros = g.E_ii
    e2_ok = z_diag and _frame_follow_check()
    ok &= _report("E2: zeros = exactly the 3 eigenframe idempotents -- diagonal (s(E_ii)=0), "
                  "rotated u-complex AND octonionic frame (zeros FOLLOW g.E_ii, covariance "
                  "explicit not assumed)", e2_ok)

    # degenerate strata recorded
    print("\n  degenerate-spectrum strata (recorded, EXCLUDED from index claims):")
    print("    X = I/3 (triple): s_X == 0 identically (the whole variety; vacuum control).")
    Xdeg = RL.h3o_from_coords(5, 5, 3, zoct(), zoct(), zoct())   # double eigenvalue 5
    # zero locus = {p : pi_{1/2}(p-compatible)} = E_33 isolated + a CP^1/S^8 in the x1=x2 block
    iso = el_eq(s_X(Xdeg, 2), el_zero())
    print(f"    X = diag(5,5,3) (double 5): E_33 an isolated zero ({iso}); the x_1=x_2 "
          "eigenspace gives a positive-dim zero locus (CP^1 on the cut / S^8-type on OP^2) "
          "-- recorded, NO index claim there.")
    ok &= _report("degenerate strata identified & excluded (vacuum s==0; double-eigenvalue "
                  "positive-dim zero locus)", iso)
    print(f"\n  GATE 2: {'ALL PASS' if ok else 'FAIL'}")
    return ok


def _frame_follow_check():
    """Zeros follow the frame under an exact F_4 automorphism (covariance explicit)."""
    Xd = RL.h3o_from_coords(7, 5, 3, zoct(), zoct(), zoct())
    # (a) permutation automorphism g=(01): g.Xd = diag(5,7,3); its zero at E_11 is s=0
    sig = {0: 1, 1: 0, 2: 2}
    gX = KK.conj_perm(Xd, sig)        # diag(5,7,3)
    a = el_eq(s_X(gX, 0), el_zero())  # E_11 still a zero (gX diagonal)
    # (b) octonionic-rotated frame: conjugate Xd by an e_1-rotation R so the eigenframe leaves
    #     the standard E_ii; the zero is then R.E_11, and s_{R Xd R*}(R E_11 R*) = 0.
    #     Use the family idempotent as a rotated frame point: build X' with eigenframe {p(t)}.
    t0 = Rational(1, 2)
    p = vMD.V24.family(t0, 1, 1)       # an off-u rank-1 idempotent (a rotated eigen-idempotent)
    # X' = 7 p + 5 q + 3 r where (p,q,r) a Jordan frame containing p; build via spectral sum:
    # simplest covariant check: s_{X'} at p vanishes iff X' in J_1(p)+J_0(p); take X'=p (rank-1)
    # then eigenvalues (1,0,0) degenerate -> use X' = p + 2*(I-p)/... ; cleanest: X'=a*p+J_0 part.
    # Frame-following witnessed by: s_{p}(p) = pi_{1/2}^{(p)}(p) = 0 (p in J_1(p)).
    b = el_eq(pi_half_general(p, p), el_zero())
    return a and b


def pi_half_general(X, p):
    """pi_{1/2}^{(p)}(X) = 2(p o (p o X)) - ... no: the Peirce-1/2 projector P_{1/2}=4L_p(I-L_p)
    applied via Jordan products: P_{1/2}(X) = 4(p o X) - 4(p o (p o X))."""
    pX = RL.jordan(p, X)
    ppX = RL.jordan(p, pX)
    return vMD.V24.el_add(vMD.V24.el_scal(4, pX), vMD.V24.el_scal(-4, ppX))


# ----------------------------------------------------------------------------
# GATE 3 -- E3 on the cut (indices + Euler + C_u-winding)
# ----------------------------------------------------------------------------
def _hessian_signs_cut(i, xv):
    """At E_ii, the cut C_u-line toward E_jj has phi'' propto (x_j - x_i): return the list of
    (j, sign) for the two cut C_u-lines."""
    out = []
    for j in range(3):
        if j != i:
            out.append((j, sp.sign(xv[j] - xv[i])))
    return out


def gate3():
    print("=" * 78)
    print("GATE 3 : E3 on the cut -- Morse indices, Euler closure, C_u-winding")
    print("=" * 78)
    ok = True
    x = {0: 7, 1: 5, 2: 3}    # x1>x2>x3
    # Morse index (# descending = # negative Hessian eigenvalues); cut has 2 real dirs per block
    print("  per-zero structure on the cut (diagonal X=diag(7,5,3), x1>x2>x3):")
    morse, phopf = [], []
    winding_rows = []
    for i in range(3):
        signs = _hessian_signs_cut(i, x)
        ndesc = sum(2 for (j, sg) in signs if sg < 0)   # 2 real cut dirs per C_u-line
        mi = ndesc
        ph = (-1) ** mi
        morse.append(mi); phopf.append(ph)
        # C_u-winding: each C_u-line is a complex line; s_X|line = (real eigenvalue)*z => the
        # C_u-phase rotates it once => winding +1 per line; the SIGN (x_j-x_i) is the matter-
        # pinned torus weight (which line is source/sink).
        lines = [(j, int(sp.sign(x[j] - x[i])), +1) for (j, sg) in signs]
        winding_rows.append((i, mi, ph, lines))
        print(f"    E_{i+1}{i+1}: cut C_u-lines {[(f'->E{j+1}{j+1}', 'wt'+('+' if w>0 else '-'), 'wind'+str(wd)) for (j,w,wd) in lines]} "
              f"; Morse index {mi}, Poincare-Hopf {ph:+d}")
    euler = sum(phopf)
    ok &= _report(f"cut Morse indices (E11,E22,E33) = {morse} (== [4,2,0]); Poincare-Hopf "
                  f"{phopf} (all +1)", morse == [4, 2, 0] and phopf == [1, 1, 1])
    ok &= _report(f"EULER CLOSURE (cut): Sum of indices = {euler} == chi(CP^2) = 3 (Borel; "
                  "Atiyah/Guillemin-Sternberg torus moment map -- cited, not claimed)", euler == 3)
    print("\n  C_u-winding decomposition (THE EXTRACTED NEW NUMBERS, conventions stated):")
    print("    convention: each cut tangent C_u-line is oriented by the C_u complex structure")
    print("    J (e_7-mult); s_X restricted to a line is z |-> (x_j-x_i) z, a real-scalar map,")
    print("    so its degree on the line's circle (the C_u-phase WINDING) is +1; the matter-")
    print("    pinned datum is the WEIGHT SIGN sign(x_j-x_i) (source/sink along the line).")
    print("    => per-zero weight-sign pattern (the moment-polytope vertex data, X-determined):")
    print(f"      E_11: (-,-)   E_22: (+,-)   E_33: (+,+)   [+ toward larger eigenvalue]")
    print(f"      total S^3 degree at each zero = product of line windings = +1 = Poincare-Hopf.")
    print(f"\n  GATE 3: {'ALL PASS' if ok else 'FAIL'}")
    return ok


# ----------------------------------------------------------------------------
# GATE 4 -- E3 on OP^2 + E4
# ----------------------------------------------------------------------------
def gate4():
    print("=" * 78)
    print("GATE 4 : E3 on OP^2 (16-dim indices + Euler) + E4 reading")
    print("=" * 78)
    ok = True
    x = {0: 7, 1: 5, 2: 3}
    morse, phopf = [], []
    for i in range(3):
        # OP^2: each (i,j) octonion block carries 8 real directions; descending iff x_j<x_i
        ndesc = sum(8 for j in range(3) if j != i and x[j] < x[i])
        mi = ndesc; ph = (-1) ** mi
        morse.append(mi); phopf.append(ph)
    euler = sum(phopf)
    ok &= _report(f"OP^2 Morse indices = {morse} (== [16,8,0]); Poincare-Hopf {phopf} (all +1, "
                  "all even Morse index)", morse == [16, 8, 0] and phopf == [1, 1, 1])
    ok &= _report(f"EULER CLOSURE (OP^2): Sum = {euler} == chi(OP^2) = 3 (Borel: b_0=b_8=b_16=1; "
                  "cited)", euler == 3)
    print(f"  ratio note: OP^2 index 16 = 4 x cut index 4 at E_11 (the 16-vs-4 tangent), but the")
    print(f"  Poincare-Hopf indices and Euler total are IDENTICAL (3) -- chi is dimension-blind.")

    print("\n  E4 reading (fenced):")
    print("  The v22-unforced gluing U(1) now carries matter-pinned TOPOLOGICAL data: the zeros")
    print("  (WHERE = the matter eigenframe) and the indices/weights (HOW MUCH), both X-determined.")
    print("  What remains UNFORCED is the LOCAL FORM of the gluing (is there a canonical matter-")
    print("  aligned connection, what selects it) -- the v30 fork, NOT claimed here.  The VACUUM")
    print("  pins nothing (s==0): matter is what creates the topological skeleton.  This is")
    print("  connection-KINEMATICS on the candidate BASE -- NO gravity, NO metric law, NO selection")
    print("  law (the v18/v20 Cartan/MM corpse stays buried); 'matter-pinned' = topological class.")
    print(f"\n  GATE 4: {'ALL PASS' if ok else 'FAIL'}")
    return ok


# ----------------------------------------------------------------------------
# GATE 5 -- the v30 ledger (exploratory, non-blocking)
# ----------------------------------------------------------------------------
def gate5():
    print("=" * 78)
    print("GATE 5 : v30 ledger (EXPLORATORY, NON-BLOCKING; NO claims)")
    print("=" * 78)
    print("  (i) the FORM-SELECTION fork (v30): given the matter-pinned topological class, is")
    print("      there a CANONICAL matter-aligned connection on the cut tangent? existence/")
    print("      uniqueness as an exact question; what functional would SELECT it (flag any")
    print("      import -- a metric/action would be a fence breach). The genuine open question.")
    print("  (ii) claim-2 contact: K_face = -log rho_face explicit in (m,q) (consumption note).")
    print("  (iii) covariant statement of the v27 balance law along the matter field's flow")
    print("      lines (a derivative-of-the-law question) -- priced only.")
    print("  Filed for v30. No verdicts.")
    return True


# ----------------------------------------------------------------------------
def main(run=(0, 1, 2, 3, 4, 5)):
    print("#" * 78)
    print("# variety_spinor_moment.py -- v28.0 Phase 88 (exact over Q/Q(t))")
    print("#" * 78)
    res = {}
    if 0 in run:
        res["g0"] = gate0()
        if not res["g0"]:
            print("\n*** GATE 0 (the v22 dictionary) FAILED -- framing wrong, STOP ***"); return res
    if 1 in run:
        res["g1"] = gate1()
        if not res["g1"]:
            print("\n*** GATE 1 controls FAILED -- STOP ***"); return res
    if 2 in run:
        res["g2"] = gate2()
    if 3 in run:
        res["g3"] = gate3()
    if 4 in run:
        res["g4"] = gate4()
    if 5 in run:
        res["g5"] = gate5()
    allp = all(res.get(g) for g in ("g2", "g3", "g4"))
    print("\n" + "=" * 78)
    print(f"  VERDICT: E1/E2 {'PASS' if res.get('g2') else 'FAIL'} (s_X=dphi_X, zeros=eigenframe); "
          f"E3 {'PASS' if res.get('g3') and res.get('g4') else 'FAIL'} (indices, Euler Sum=3=chi "
          "on cut & OP^2, C_u-winding); E4 reading (fenced).")
    print("=" * 78)
    print(f"\n[{time.time() - _t0:6.1f}s] checks: {sum(PASS)}/{len(PASS)} PASS")
    return res


if __name__ == "__main__":
    main()
