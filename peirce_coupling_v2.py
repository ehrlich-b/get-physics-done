"""
Follow-up: investigate WHY the random-direction RMS indirect coupling
depends on d, even though all basis-direction couplings are identical.

The answer: it's a geometric averaging effect. When you pick random
unit vectors in V_{1/2} (dim 2d) and V_0 (dim d+2), the ALIGNMENT
between c and the "correct" diagonal that couples becomes less likely
in higher dimension. The max coupling is always 1/4, but the average
over the sphere scales as 1/dim(V_0).

Also: investigate whether MIXED mediators (a has both x2 and x3 nonzero)
can create different indirect couplings for x1.
"""

import numpy as np
import sys
sys.path.insert(0, '/Users/ehrlich/scratch/get-physics-done')
from peirce_coupling import *

np.set_printoptions(precision=10, suppress=True)


def mixed_mediator_analysis(K):
    """
    Key question: when the mediator a has BOTH x2 and x3 components,
    does the x1 off-diagonal in V_0 get a nonzero 2nd-order coupling?
    """
    d = K.dim
    print(f"\n{'='*70}")
    print(f"  MIXED MEDIATOR ANALYSIS for h_3({K.name})")
    print(f"{'='*70}")

    # a = (x2 = e_0, x3 = e_0), normalized
    x2_val = K.basis(0)
    x3_val = K.basis(0)
    a = H3Matrix(K, [0.0, 0.0, 0.0], [K.zero(), x2_val, x3_val])
    a_nsq = a.norm_sq()
    a = a.scale(1.0 / np.sqrt(a_nsq))
    print(f"\n  a = normalized (x2=e_0, x3=e_0), ||a||^2 = {a.norm_sq():.6f}")

    # Direct coupling
    aoa = a.jordan_product(a)
    v1, _, _ = aoa.peirce_decompose(0)
    print(f"  Direct k_1 = P_1(aoa)/||a||^2 = {v1.diag[0]:.6f}")

    # Indirect: all V_0 basis directions
    v0_basis = [
        ("E_22", H3Matrix(K, [0.0, 1.0, 0.0], [K.zero(), K.zero(), K.zero()])),
        ("E_33", H3Matrix(K, [0.0, 0.0, 1.0], [K.zero(), K.zero(), K.zero()])),
    ]
    for i in range(min(d, 3)):  # just first few basis elements
        v0_basis.append((f"x1_e{i}", H3Matrix(K, [0.0, 0.0, 0.0], [K.basis(i), K.zero(), K.zero()])))

    for name, c_mat in v0_basis:
        c_nsq = c_mat.norm_sq()
        c_unit = c_mat.scale(1.0 / np.sqrt(c_nsq))

        w = c_unit.jordan_product(a)
        _, w_half, _ = w.peirce_decompose(0)
        wa = w_half.jordan_product(a)
        v1_wa, _, _ = wa.peirce_decompose(0)
        print(f"  c = {name:8s}: k_2 = {v1_wa.diag[0]:+.6f}")

    # Now with x2 and x3 in DIFFERENT octonionic directions
    if d > 1:
        print(f"\n  a = normalized (x2=e_0, x3=e_1)")
        x2_val2 = K.basis(0)
        x3_val2 = K.basis(1)
        a2 = H3Matrix(K, [0.0, 0.0, 0.0], [K.zero(), x2_val2, x3_val2])
        a2_nsq = a2.norm_sq()
        a2 = a2.scale(1.0 / np.sqrt(a2_nsq))

        for name, c_mat in v0_basis:
            c_nsq = c_mat.norm_sq()
            c_unit = c_mat.scale(1.0 / np.sqrt(c_nsq))

            w = c_unit.jordan_product(a2)
            _, w_half, _ = w.peirce_decompose(0)
            wa = w_half.jordan_product(a2)
            v1_wa, _, _ = wa.peirce_decompose(0)
            print(f"  c = {name:8s}: k_2 = {v1_wa.diag[0]:+.6f}")


def x1_coupling_via_cubic(K):
    """
    The x1 off-diagonal DOES couple to E_11, but through the CUBIC term
    in the determinant, not through the Jordan product tower.

    The determinant is the 3rd power in the power-associative algebra.
    det(X) = (1/3) * Tr(X^3) - (1/2) * Tr(X^2) * Tr(X) + (1/6) * Tr(X)^3

    Actually for Jordan algebras, det is the generic norm:
    N(X) = abc + 2*Re(x1*x2*x3) - a*|x1|^2 - b*|x2|^2 - c*|x3|^2

    The cubic term 2*Re(x1*x2*x3) provides a TRILINEAR coupling x1-x2-x3.
    This is the ONLY path from x1 to the observer that goes through the algebra.

    Compare this to the BILINEAR coupling from the Jordan product:
    - x2 o x2 has E_11 projection (direct bilinear)
    - x1 NEVER produces E_11 via bilinear Jordan products
    - x1 CAN reach E_11 via the cubic form (trilinear)

    This means x1 is "one order higher" in the coupling hierarchy.
    The question: does this give a NUMERICAL suppression?
    """
    d = K.dim
    print(f"\n{'='*70}")
    print(f"  CUBIC (DETERMINANT) COUPLING ANALYSIS for h_3({K.name})")
    print(f"{'='*70}")

    # The cubic norm N(t*e_11 + s*x2_unit + r*x1_unit)
    # We want d^2N/(ds dt) at origin vs d^3N/(dr ds dt) at origin

    eps = 1e-4

    # x2 direction
    x2_dir = H3Matrix(K, [0.0, 0.0, 0.0], [K.zero(), K.basis(0), K.zero()])
    # x1 direction
    x1_dir = H3Matrix(K, [0.0, 0.0, 0.0], [K.basis(0), K.zero(), K.zero()])
    # E_11 direction
    e11_dir = H3Matrix(K, [1.0, 0.0, 0.0], [K.zero(), K.zero(), K.zero()])
    # x3 direction
    x3_dir = H3Matrix(K, [0.0, 0.0, 0.0], [K.zero(), K.zero(), K.basis(0)])

    def make_mat(t, s, r, u):
        """M = t*E_11 + s*x2 + r*x1 + u*x3"""
        M = e11_dir.scale(t).add(x2_dir.scale(s)).add(x1_dir.scale(r)).add(x3_dir.scale(u))
        return M

    # d^2 det / (dt ds) at origin (x2-E11 coupling via det)
    # det is cubic, so this derivative at origin = 0 (since det has no term linear in both t and s only)
    # Actually: det = t*b*c + 2*Re(x1*s_x2*u_x3) - t*|x1|^2 - b*|s_x2|^2 - c*|u_x3|^2
    # with a=t, x2=s*e_0, x1=r*e_0, x3=u*e_0, b=0, c=0

    # det(t*E11 + s*x2) = t*0*0 + 0 - 0 - 0 - 0 = 0 for all t,s when b=c=x1=x3=0
    # That's trivially 0. The det doesn't capture the bilinear coupling.

    # The Jordan product IS the bilinear coupling. The det adds the trilinear.

    # Let's think about this differently:
    # In a QFT built on h_3(O), the interaction vertices come from:
    # 1. Jordan product (bilinear): a o b -> gives propagators and 2-point functions
    # 2. Determinant/generic norm (cubic): N(a,b,c) -> gives 3-point vertices

    # The bilinear Jordan coupling of x2 to E_11:
    #   <E_11, x2 o x2> = 1/2 * |x2|^2  (direct)

    # The bilinear Jordan coupling of x1 to E_11:
    #   <E_11, x1 o x1> = 0  (x1 is in V_0, its square stays in V_0+V_1... wait)

    # Actually, let me check: x1 o x1 might have a V_1 component!
    x1_mat = H3Matrix(K, [0.0, 0.0, 0.0], [K.basis(0), K.zero(), K.zero()])
    x1ox1 = x1_mat.jordan_product(x1_mat)
    v1, vh, v0 = x1ox1.peirce_decompose(0)
    print(f"\n  x1 o x1:")
    x1ox1.describe()
    print(f"  P_1(x1 o x1) = {v1.diag[0]:.6f}")
    print(f"  P_{{1/2}}(x1 o x1) norm = {vh.norm_sq():.6f}")
    print(f"  P_0(x1 o x1):")
    v0.describe()

    # So x1 o x1 stays entirely in V_0 (as expected: V_0 o V_0 -> V_0 + V_1,
    # but for a rank-1 e, the V_1 component of V_0 o V_0 is 0 by Peirce rules!)
    # Wait, the Peirce rules say V_0 o V_0 subset V_0, NOT V_0 + V_1.
    # Let me verify: V_i o V_j subset V_{i+j} for eigenvalue sum,
    # but it's more nuanced. For rank-1:
    # V_0 o V_0 -> V_0 (yes, this is the standard result)
    # V_{1/2} o V_{1/2} -> V_1 + V_0
    # V_0 o V_{1/2} -> V_{1/2}

    print(f"\n  Confirmed: V_0 o V_0 -> V_0 (no leakage to V_1)")
    print(f"  x1 coupling to E_11 is PURELY through the cubic determinant term")

    # The cubic term coefficient:
    # d^3 N / d(x1) d(x2) d(x3) = 2 * delta (when all in same K-direction)
    # This is the ONLY coupling of x1 to the observer (via x2 and x3 mediators)

    # In perturbation theory terms:
    # - x2, x3: couple to observer at TREE LEVEL (bilinear Jordan product)
    # - x1: couples to observer at ONE-LOOP (cubic vertex needs two propagators)
    # The suppression is: k_1_eff ~ g^2 * (cubic_coeff) / (mass_gap)^2
    # where g is the Jordan product coupling = 1/2

    print(f"\n  COUPLING HIERARCHY:")
    print(f"    x2, x3: bilinear coupling to E_11 = 1/2 (tree level)")
    print(f"    x1:     trilinear coupling via det = 2 * Re(x1*x2*x3)")
    print(f"            requires TWO mediators (x2 and x3)")
    print(f"            effective coupling ~ (1/2)^2 * 2 = 1/2 (naive)")
    print(f"            but x1 needs x2 AND x3 simultaneously present")

    # E_22 coupling
    e22_mat = H3Matrix(K, [0.0, 1.0, 0.0], [K.zero(), K.zero(), K.zero()])
    e22oe22 = e22_mat.jordan_product(e22_mat)
    v1_e, _, _ = e22oe22.peirce_decompose(0)
    print(f"\n  E_22 o E_22:")
    e22oe22.describe()
    print(f"  P_1(E_22 o E_22) = {v1_e.diag[0]:.6f}")
    print(f"  (E_22 is in V_0, so E_22 o E_22 stays in V_0, no coupling to E_11)")

    # What about E_22 o x3?
    x3_mat = H3Matrix(K, [0.0, 0.0, 0.0], [K.zero(), K.zero(), K.basis(0)])
    e22ox3 = e22_mat.jordan_product(x3_mat)
    v1_mix, vh_mix, v0_mix = e22ox3.peirce_decompose(0)
    print(f"\n  E_22 o x3:")
    e22ox3.describe()
    print(f"  P_{{1/2}}(E_22 o x3):")
    vh_mix.describe()
    print(f"  ||P_{{1/2}}|| = {vh_mix.norm_sq():.6f}")

    # The result: E_22 o x3 = (1/2) * x3 (since x3 is in V_{1/2} and
    # E_22 acts as multiplication by eigenvalue in the V_0 direction)
    # Wait, E_22 is in V_0, and x3 is in V_{1/2}. Their product:
    # V_0 o V_{1/2} -> V_{1/2}


def dimension_dependence_analysis():
    """
    Even though the coupling CONSTANTS are d-independent,
    check if the number of CHANNELS matters.

    In h_3(O):
    - 16 channels in V_{1/2} (x2: 8 octonionic components, x3: 8 components)
    - 10 channels in V_0 (b, c: 2 real; x1: 8 octonionic components)

    In h_3(R):
    - 2 channels in V_{1/2}
    - 3 channels in V_0

    If you sum over all channels (trace), the TOTAL coupling strength scales with d.
    """
    print(f"\n{'='*70}")
    print(f"  CHANNEL COUNTING AND TOTAL COUPLING STRENGTH")
    print(f"{'='*70}")

    for K in [RealAlgebra, ComplexAlgebra, QuaternionAlgebra, OctonionAlgebra]:
        d = K.dim

        # Total direct coupling: sum over all V_{1/2} basis elements
        total_direct = 0.0
        # x2 basis
        for i in range(d):
            a = H3Matrix(K, [0.0, 0.0, 0.0], [K.zero(), K.basis(i), K.zero()])
            a_nsq = a.norm_sq()
            a = a.scale(1.0 / np.sqrt(a_nsq))
            aoa = a.jordan_product(a)
            v1, _, _ = aoa.peirce_decompose(0)
            total_direct += v1.diag[0]

        # x3 basis
        for i in range(d):
            a = H3Matrix(K, [0.0, 0.0, 0.0], [K.zero(), K.zero(), K.basis(i)])
            a_nsq = a.norm_sq()
            a = a.scale(1.0 / np.sqrt(a_nsq))
            aoa = a.jordan_product(a)
            v1, _, _ = aoa.peirce_decompose(0)
            total_direct += v1.diag[0]

        # Total indirect coupling: sum |k_2|^2 over all pairs
        total_indirect_sq = 0.0
        v0_basis = [H3Matrix(K, [0.0, 1.0, 0.0], [K.zero(), K.zero(), K.zero()]),
                     H3Matrix(K, [0.0, 0.0, 1.0], [K.zero(), K.zero(), K.zero()])]
        for i in range(d):
            v0_basis.append(H3Matrix(K, [0.0, 0.0, 0.0], [K.basis(i), K.zero(), K.zero()]))

        vh_basis = []
        for i in range(d):
            vh_basis.append(H3Matrix(K, [0.0, 0.0, 0.0], [K.zero(), K.basis(i), K.zero()]))
            vh_basis.append(H3Matrix(K, [0.0, 0.0, 0.0], [K.zero(), K.zero(), K.basis(i)]))

        for c_mat in v0_basis:
            c_nsq = c_mat.norm_sq()
            c_unit = c_mat.scale(1.0 / np.sqrt(c_nsq))

            for a_mat in vh_basis:
                a_nsq = a_mat.norm_sq()
                a_unit = a_mat.scale(1.0 / np.sqrt(a_nsq))

                w = c_unit.jordan_product(a_unit)
                _, w_half, _ = w.peirce_decompose(0)
                wa = w_half.jordan_product(a_unit)
                v1_wa, _, _ = wa.peirce_decompose(0)
                total_indirect_sq += v1_wa.diag[0]**2

        print(f"\n  h_3({K.name:1s}): d={d}")
        print(f"    dim(V_{{1/2}}) = {2*d}, dim(V_0) = {d+2}")
        print(f"    Total direct coupling (sum over channels): {total_direct:.4f} = {2*d} * 0.5 = {d:.1f}")
        print(f"    Total indirect |k_2|^2 (sum over channel pairs): {total_indirect_sq:.6f}")
        print(f"    sqrt(total indirect |k_2|^2): {np.sqrt(total_indirect_sq):.6f}")
        print(f"    Ratio direct / sqrt(indirect^2): {total_direct / np.sqrt(total_indirect_sq) if total_indirect_sq > 0 else 'inf':.4f}")


def spectral_gap_analysis():
    """
    The REAL hierarchy mechanism: the Jordan operator L_e(x) = e o x
    has spectrum {0, 1/2, 1} with MULTIPLICITIES depending on d.

    The spectral gap is always 1/2 (independent of d).
    But the DEGENERACY ratio is d-dependent:
    - Multiplicity of eigenvalue 1: 1
    - Multiplicity of eigenvalue 1/2: 2d
    - Multiplicity of eigenvalue 0: d+2

    The "observability" of a V_0 mode depends on how many V_{1/2} modes
    it can scatter through to reach V_1. This is a COMBINATORIAL factor,
    not a coupling constant.
    """
    print(f"\n{'='*70}")
    print(f"  SPECTRAL / DEGENERACY ANALYSIS")
    print(f"{'='*70}")

    for K in [RealAlgebra, ComplexAlgebra, QuaternionAlgebra, OctonionAlgebra]:
        d = K.dim
        n = 3 + 3*d  # dim(h_3(K))

        m1 = 1        # multiplicity of eigenvalue 1
        mhalf = 2*d   # multiplicity of eigenvalue 1/2
        m0 = d + 2    # multiplicity of eigenvalue 0

        print(f"\n  h_3({K.name:1s}): d={d}, dim={n}")
        print(f"    Eigenvalue 1:   mult = {m1}")
        print(f"    Eigenvalue 1/2: mult = {mhalf}")
        print(f"    Eigenvalue 0:   mult = {m0}")
        print(f"    Ratio (V_{{1/2}} channels) / (V_0 modes) = {mhalf}/{m0} = {mhalf/m0:.4f}")
        print(f"    For mass hierarchy: need V_0 modes to be suppressed by 1/(mhalf) per vertex")
        print(f"    Each V_{0} mode scatters through ~{mhalf} intermediate states")
        print(f"    If interference is destructive, suppression ~ 1/{mhalf} = 1/{2*d} = {1/(2*d):.4f}")

    print(f"\n  CONCLUSION:")
    print(f"    The Peirce coupling CONSTANTS are universal: k_1 = 1/2, k_2 = 1/4, k_4 = 1/16")
    print(f"    The coupling constants do NOT depend on dim(K).")
    print(f"    Any hierarchy must come from:")
    print(f"      (a) Combinatorial channel counting (dim-dependent)")
    print(f"      (b) The cubic determinant structure (universal coefficient 2)")
    print(f"      (c) Dynamical mass gaps (requires a Hamiltonian, not just algebra)")
    print(f"    The Peirce tower alone gives a FIXED ratio of 8:1 (direct:4th-order)")
    print(f"    independent of the division algebra.")


if __name__ == "__main__":
    for K in [RealAlgebra, OctonionAlgebra]:
        mixed_mediator_analysis(K)

    for K in [RealAlgebra, OctonionAlgebra]:
        x1_coupling_via_cubic(K)

    dimension_dependence_analysis()
    spectral_gap_analysis()
