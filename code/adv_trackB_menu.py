"""ATTACK 3 — Track B completeness. Try to NAME a native functional producing Einstein WITHOUT
being the a_1=int R sqrt(g) import. Analyze each candidate for (a) selection-traceability and
(b) whether delta^2/delta g^2 yields the Einstein operator (Delta_L - 2Lambda) on the TT sector.

This is an analytic argument (variational calculus of spectral functionals); SHORT and decisive.
"""
print("="*78)
print("ATTACK 3: candidate native functionals the menu might have missed")
print("="*78)

cands = [
("Combination of eigenvalues  f(lambda_1,...,lambda_k)",
 "selection-traceable? YES (the lambda-tower is native via the moment embedding).",
 "produces Einstein? NO. The first variation of ANY eigenvalue lambda_n[g] on the TT sector is\n"
 "   delta lambda_n[h] = -<dphi_n (x) dphi_n , h>  (Berger/El Soufi-Ilias), a GRADIENT-PRODUCT\n"
 "   stress, NOT the Einstein tensor. A smooth f of several lambda_n is a linear combo of such\n"
 "   gradient products (chain rule) => image still in span{dphi (x) dphi} = Sym^2(8), the SAME\n"
 "   27-once space as Track A. Its 2nd variation is the SAME lambda-Hessian family (Schur-locked\n"
 "   on one irrep). So a lambda-combination is just Track A in disguise: NOT a new Einstein-producer.\n"
 "   [The degeneracy-split of Attack 1 also applies: lambda_1 splits, lambda_2=32 is the matter\n"
 "    mode's OWN eigenvalue (its variation is again a gradient product). No escape.]"),

("Higher matter functional  int |grad phi_M|^4  or  int |F_moment|^2 (YM-type)",
 "selection-traceable? PARTIAL (phi_M is native, but the POWER/contraction choice is a free input\n"
 "   -- why 4th power? why YM? no algebra datum selects it; this is a model-building choice = IMPORT-like).",
 "produces Einstein? NO. int |grad phi|^4 -> delta/delta g gives a stress quadratic in (grad phi)(x)(grad phi),\n"
 "   i.e. (Sym^2(8))^(x)2 content -- a HIGHER-rank tensor in the matter, NOT the universal Delta_L.\n"
 "   The Einstein operator is matter-INDEPENDENT (acts as 20 on EVERY block regardless of M); a\n"
 "   |grad phi|^4 stress is matter-direction-dependent. Cannot be (Delta_L-2Lambda)."),

("Spectral zeta / log-determinant  zeta'(0) = -log det Delta",
 "selection-traceable? NO. The zeta-determinant requires the functional-integral/heat-kernel\n"
 "   regularization machinery (a choice of operator Delta, a choice of regularization) -- exactly\n"
 "   the v21 kind-4 (base-Sakharov) IMPORT. NOT native (the extremize-effective-action is imported).",
 "produces Einstein? Its metric variation is delta log det Delta = int a_1-density-type terms\n"
 "   = the SAME int R sqrt(g) heat-kernel coefficient (Polyakov/Gilkey) PLUS higher a_k. So at the\n"
 "   leading 2-derivative order it REPRODUCES a_1 = int R sqrt(g) -- i.e. it IS the import a_1\n"
 "   (Trap #22), already on the menu and fenced. v21 killed this route (Gate 2 support-mismatch)."),

("Total scalar curvature via a 'framework-selected' spectral route  (a_1 in costume)",
 "selection-traceable? NO. a_1's coefficient is universal (Gilkey 1/(4pi)^2 int R/6); NO framework\n"
 "   datum picks a_1 over a_0=Vol or a_2=curvature^2. Wearing a spectral costume does not make the\n"
 "   SELECTION native. (The RESEARCH explicitly flags this as the dead GST move.)",
 "produces Einstein? YES (it IS int R sqrt(g)) -- but precisely as the IMPORT. Not native."),

("a_2 heat invariant (R^2, |Ric|^2, |Riem|^2)",
 "selection-traceable? NO (same as a_1: universal coefficients, no framework selection).",
 "produces Einstein? NO -- a_2 is 4-derivative (Bach/quadratic-gravity), NOT the 2-derivative\n"
 "   Einstein operator. Out of scope and not Einstein anyway."),
]
for name,sel,prod in cands:
    print(f"\n* {name}\n  {sel}\n  {prod}")

print("\n"+"="*78)
print("CONCLUSION (Attack 3): every named candidate either")
print("  (a) reduces to Track A (lambda-tower / gradient-product stress, Schur-locked, not Einstein), OR")
print("  (b) is the a_1 = int R sqrt(g) IMPORT in disguise (zeta-det, spectral-costume scalar curvature), OR")
print("  (c) is matter-dependent / higher-rank / higher-derivative (NOT the universal Delta_L-2Lambda).")
print("No native functional A[g] produces the Einstein operator. The menu is complete.")
print("=> Attack 3 CONFIRMS the negative verdict.")
