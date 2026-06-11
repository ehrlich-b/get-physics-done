# 85 — RESEARCH: The Moment Doublet and the Canonical Field Equation on the Event-Space

**v25.0 Phase 85 (J5-on-the-variety, step 1). Verification-and-extraction milestone.
Drivers: `code/variety_moment_doublet.py` (executor, 27/27 PASS, 20.6 s),
`code/variety_moment_doublet_verify.py` (independent path, 11/11 PASS). Exact over
Q / Q(t). VERDICT: C1 PASS, C2 PASS (λ₁ = 48 on OP², 12 on the CP² cut), C3 PASS.**

This run reads the entire v24.0 entropy landscape as the **moment doublet** of the
linear pair `(X, X#)` over the idempotent variety, and shows the doublet obeys a
**forced, matter-independent, first-order (Helmholtz) field equation** on the frozen
canonical (Borel) geometry. It is the *entropy side* of a would-be J5 balance, not
the balance. Background geometry is imported as math; no G = κT, no Newton constant,
no SUGRA dynamics (the library note that X# "is the field equation of 5d magic
supergravity" is a recorded curiosity, fenced — nothing here imports SUGRA).

---

## 1. Setup and objects (all in the repo's frozen conventions)

Algebra `h_3(O)` in the engine layout (`ring_lemma_verification.py`):
```
        | alpha     conj(x3)   x2      |
    X = | x3        beta       conj(x1)|       Tr(X) = alpha+beta+gamma,
        | conj(x2)  x1         gamma   |        X∘Y = (XY+YX)/2  (Jordan),
```
cubic norm `N(X) = det_3(X) = αβγ − α|x1|² − β|x2|² − γ|x3|² + 2Re((x2 x1)x3)`
(the F₄-invariant generic norm; cross-term factor order `(x2 x1)x3` is the Phase-64.1
fix, det SSOT = `RL.det_3`). Trace form `⟨A,B⟩ := Tr(A∘B)`. `u = e_7`, the cut algebra
`C_u = span{1, e_7} ≅ ℂ`.

**The event-space** is the primitive-idempotent variety
`OP² = {rank-1 idempotents} = F_4/Spin(9)` (Cayley plane, dim 16), with the totally
geodesic **CP² cut** `= {rank-1 idempotents of h_3(C_u)} = SU(3)/U(2)`, dim 4, tangent
`{11,18,19,26}` (the v24 bottleneck `OP² → CP²`).

**The v24 face object.** For a rank-1 idempotent `p` and a state `X`, the Peirce-0
compression onto the rank-2 complement face `V_0(p) = h_2(O)` is
`C_p X = P_0(p)·X = 2(p∘(p∘X)) − 3(p∘X) + X` (since `L_p` has spectrum `{0,½,1}`,
`P_0 = 2L_p² − 3L_p + 1`). v24's verdict object is the normalized face purity
`r(p) = det_2(C_p X)/Tr(C_p X)²`, with `det_2(Y) = (Tr(Y)² − Tr(Y∘Y))/2`.

**The Freudenthal sharp / adjugate.** `X# = X × X`, where the cross product
(`h3o-math-library.md §5`) is
```
X × Y = X∘Y − ½(Tr(X)Y + Tr(Y)X) + ½(Tr(X)Tr(Y) − Tr(X∘Y)) I
```
so the diagonal `X# = X∘X − Tr(X)X + σ₂(X) I`, with `σ₂(X) = ½(Tr(X)² − Tr(X∘X))`
the second char-poly coefficient. We build `X#` **only** from `RL.jordan/Tr/identity`
(no new convention surface), and pin it to the repo by the three classical defining
identities, all verified exactly:
- adjugate: `(X#)# = N(X)·X`;
- gradient-of-norm: `Tr(X#∘Y) = 3N(X,X,Y) = ½·d(X,X,Y)` (`d` = `RL.polarize_d`);
- `Tr(X#) = σ₂(X)`, and the rank-1 characterization `E_11# = 0`, `Tr E_11 = 1`.
The independent verifier reconstructs `X#` the *other* way — from the cubic-norm
gradient `⟨X#,E_a⟩ = ½ d(X,X,E_a)` via the trace-form Gram dual — and agrees.

The identity below is presumably **classical cubic-Jordan theory** (the adjugate /
cofactor identity); novelty is **not** claimed for the identity. The program content
is the *doublet reading* of v24 plus C2/C3.

---

## 2. C1 — the moment-doublet identity (the core)

> **For all `X ∈ h_3(O)` and all rank-1 idempotents `p`:**
> **`m(p;X) := Tr(C_p X) = Tr(X) − ⟨X,p⟩`**  and  **`q(p;X) := det_2(C_p X) = ⟨X#,p⟩`.**

Because the rank-2 face state has exactly two spectral invariants (trace and
determinant of a spin-factor element), `(m, q)` **generate** the whole v24 object:
`r = q/m²`, and the full normalized face char-poly is a function of `(m,q)` alone.
**Consequence: the entire v24 landscape is the moment doublet of `(X, X#)` — two
linear moment fields over the event-space, nothing else.**

**Derivation (worked, three steps).**
- *(i) the trace moment.* `m = Tr(C_p X) = Tr(P_0(p)X)`. `P_0(p) = U_{1−p}` is
  trace-self-adjoint, `U_{1−p}1 = (1−p)` (since `1−p` is idempotent), so
  `Tr(P_0(p)X) = ⟨X, P_0(p)1⟩ = ⟨X, 1−p⟩ = Tr(X) − ⟨X,p⟩`. (Equivalently: at the base
  point `p = E_11`, `C_p X` is the lower 2×2 block `(β,γ,x1)`, `Tr = β+γ = Tr(X) − α`,
  and `⟨X,E_11⟩ = α`.)
- *(ii) the determinant moment at the base point.* At `p = E_11` the complement face
  is the lower 2×2 block `[[β, conj(x1)],[x1, γ]]`; its rank-2 determinant is
  `βγ − |x1|²`, which is exactly the (1,1) cofactor of `X` = `(X#)_{11} = ⟨X#, E_11⟩`.
  Verified literally (the independent verifier computes `βγ − |x1|²` and `⟨X#_gradN,
  E_11⟩` by two separate routes and they agree for symbolic `X`).
- *(iii) extension to all `p` by F₄-covariance.* F₄ = Aut(h_3(O)) preserves `∘`, `Tr`,
  `N`, hence commutes with `#` and maps compressions to compressions, and acts
  **transitively** on rank-1 idempotents (Freudenthal–Borel 1950). Every `p = g·E_11`
  for some `g ∈ F_4`, and both sides are F₄-covariant:
  `m(g·E_11; X) = m(E_11; g⁻¹·X)`, `q(g·E_11; X) = q(E_11; g⁻¹·X)`. So C1 at `E_11`
  for *symbolic* `X` (proven, 27 free params) closes to **all `p`** for all `X`. ∎

**How it was actually verified (no shortcut taken on faith).** C1 was checked (a) at
`E_11`, symbolic `X` (27 params); (b) along **all 16** families `(j,k)`,
`j∈{1,2}, k∈0..7`, with symbolic `X` over `Q(t)` — *including the off-u families*
`(1,1)..(1,6),(2,1)..(2,6)` — directly, with no covariance shortcut; (c) the
covariance relation `φ_Y(g·p) = φ_{g⁻¹Y}(p)` spot-checked exactly for `g ∈ {(01),(012)}`,
`Y ∈ {X, X#}`, off-u sample points. The independent path re-checks C1 at `E_11`
(symbolic) and along `(1,1)` over `Q(t)` using the **eigenprojector** compression and
the **gradient-of-N** sharp.

**Completeness — all of v24 from one identity (reproduced exactly):**
- *(a) vacuum, now DERIVED:* `(I/3)# = I/9`, so `q ≡ 1/9`, `m ≡ 2/3`, `r ≡ 1/4`
  everywhere. The vacuum is homogeneous **because both moments of `(I/3, (I/3)#)` are
  constant** — not an accident.
- *(b) diagonal direction-blindness, DERIVED:* for diagonal `X`, `X#` is diagonal, so
  `q = ⟨X#,p⟩` sees only `diag(p)` and `|offdiag(p)|²`; the octonion slot `e_k` enters
  a family's `(0,1)` entry only through `|s·e_k|² = s²`, **independent of `k`** — the
  three `(0,1)` families give identical `(m,q)`, hence identical `r`. (The octonion
  direction enters the moments *only* through the off-diagonal entries of `X`/`X#`,
  which vanish for diagonal `X`.)
- *(c) generic-X tables reproduced from the doublet:* off-u `r(2) = 2727493/12700800`,
  C_u-phase `r(3) = 503003/2252432` — exact match to the recorded 84-GATE-2 values.
- *(d) eigenframe critical points:* transverse-real `(1,0)` gives `dr/dt = 0` at
  `{−1,0,1}` (the standard frame); the matter-coupled `(1,7),(1,1)` give degree-≥5
  numerators (CRootOf, the rotated matter eigenframe) — the v24 finding, now read off
  the alignment of the two frequency-2 trigs in `(m,q)`.
- *(e) flattening, DERIVED:* `X_s = (1−s)I/3 + sX_gen` gives moments affine in `s`
  around the constant vacuum moments, so the landscape gradient `dr/dτ|_0` vanishes at
  `s=0` and grows with matter (recorded table: `0, 13879/1837500, …, 629/58800`).

---

## 3. C2 — the forced canonical field equation

Linear moment functions restricted to the variety span exactly
`{constants} ⊕ {first canonical Laplace level}`: on `OP²`, `h_3(O)* = 27 = 1 ⊕ 26`
under F₄ (rank-1 idempotents span the algebra; `⟨1,p⟩ ≡ 1` is the constant; the `26`
is the first spherical harmonic of the two-point homogeneous space `OP²`,
multiplicity-free L², Cartan/Helgason). On the CP² cut, `h_3(C_u)* = 9 = 1 ⊕ 8` under
SU(3), same structure (the `(1,1)` harmonics). Therefore **every** moment field
`φ_Y(p) = ⟨Y,p⟩` obeys the canonical Helmholtz equation

> **`Δ(φ_Y − φ̄_Y) = −λ₁ (φ_Y − φ̄_Y)`,  `φ̄_Y = ⟨Y, I/3⟩`**

(the mean is exact, no integration: `I/3` is the F₄-average of `p` by invariance), with
`λ₁` fixed by the canonical geometry alone — **matter-independent / universal**.

**Sharpest form (all `Y` at once, at `E_11`).** Since `φ_Y` is linear in `p`,
`Δφ_Y(E_11) = ⟨Y, ΔP⟩` where `ΔP := Σ_i ¼ p_i''(0)` is the mean-curvature vector
(trace of the second fundamental form) over an orthonormal canonical-geodesic frame.
The whole of C2 is then the single h_3(O)-vector identity
> **`ΔP = −λ₁ (E_11 − I/3)`.**

Computed exactly (both code paths, two different frames, λ extracted from the `E_11`
and independently the `E_22` component):
```
   OP² (16-frame):  ΔP = diag(−32, 16, 16) = −48 (E_11 − I/3)   ⇒  λ₁ = 48
   CP² cut (4-frame): ΔP = diag(−8,  4,  4) = −12 (E_11 − I/3)   ⇒  λ₁ = 12
```
Each direction contributes `−2` to `Δc11` (the c11 = cos²θ unit-speed certificate,
`(1/4)·c11''_t(0) = −2`); 16 vs 4 directions give `Δc11 = −32` vs `−8`, and
`c11(E_11) − c̄ = 1 − 1/3 = 2/3`, so `λ₁ = 48` and `12`.

**Pre-registered eigenvalues CONFIRMED.** `λ₁(CP²) = 12 = 4(n+1)|_{n=2}` matches the
Fubini–Study spectrum `λ_j = 4j(j+n)` (j=1) — a free external cross-check
(Ikeda–Taniguchi 1978; Berger–Gauduchon–Mazet). `λ₁(OP²) = 48` (Cayley plane
`F_4/Spin(9)`, canonical/Borel normalization in which the totally geodesic CP² cut
gives 12). The ratio `λ₁(OP²)/λ₁(CP²) = 4 = 16/4 = dim ratio`.

**Field equations in final form** (means `m̄ = (2/3)Tr X`, `q̄ = σ₂(X)/3 = Tr(X#)/3`,
both verified for symbolic X):
> **`Δ m = −λ₁ (m − (2/3) Tr X)`,  `Δ q = −λ₁ (q − σ₂(X)/3)`,  λ₁ = 48 (OP²) / 12 (cut).**
The state's second char-poly coefficient `σ₂(X)` is the background level of the `q`
field — matter (via `X#`) sources the doublet; the geometry fixes the operator.

---

## 4. C3 — the geodesic-frequency fingerprint

Level ≤ 1 ⟺ the restriction of `φ_Y` to every closed canonical geodesic is
`a + b·cos2θ + c·sin2θ` (frequency ≤ 2; `t = tan(θ/2)` the rational chart) ⟺
`moment·(1+t²)²` is a polynomial in `t` of degree ≤ 4. Verified for `m, q` (symbolic
X) on all cut and off-u families. Hand anchor: `diag(7,5,3)` on `(1,0)` gives
`m = 9 − cos2θ`, `q = 18 − 3cos2θ` exactly. The v24 `r = q/m²` is then a ratio of
frequency-2 trigs over a squared one — a **rational** function with infinite harmonic
content, which is **why** no field equation is claimed for `r` (trap-guard #5; the
contentful objects are the unnormalized `(m,q)`). Discriminating control: `c11² = cos⁴θ`
(frequency 4) **fails** the ≤2 test — the test can say no.

---

## 5. Trap-class guards (binding) and anti-overclaim

- **#5 (rational-function trap):** `r = q/m²` is rational; no field equation is claimed
  for `r`. The verdict objects are the unnormalized doublet `(m,q)`. Held.
- **#6 (annihilator trap):** only the first-order single-eigenvalue (Helmholtz)
  statement is reported; no polynomial-in-Δ annihilator is called a law. Held.
- **Convention drift:** the `#` and trace-form conventions are the repo's; the
  compression is the v24 code path; recorded v24 tables reproduced first (the
  convention-vs-substance triage). Held (independent path reproduces anchors too).
- **Frame/normalization:** no family enters a frame without the c11-form certificate;
  Δ is frame-independent (rotated cut frame + entry-swap Spin(9), both agree). Held.
- **Numeric leakage:** every verdict is symbolic/exact over Q or Q(t). Held.

**Anti-overclaim (binding scope).** PASS ≠ Einstein, ≠ J5, ≠ a balance, ≠ dynamics.
The background geometry is FROZEN (Borel's metric, imported as math); this run
certifies the matter field's canonical **type** (a level-≤1 moment doublet of `(X,X#)`)
and its forced linear field equation on that fixed background — the *entropy side* of
a would-be balance, not the balance. `λ₁` is a property of the canonical geometry, not
a derived coupling; no Newton constant exists here. The identity C1 is classical Jordan
theory (cited, not claimed). Signature remains OPEN (the variety is Riemannian/compact;
its role as the candidate event-space is unchanged). Family-sampled differential claims
are closed by the covariance argument (stated where it carries the load). The
deflation stands: the landscape's harmonic finiteness is automatic once C1 holds; the
CONTENT is (i) the doublet characterization (all of v24 from one identity), (ii) the
single-level fact with universal `λ₁`, (iii) the exact eigenvalues 48 and 12, (iv) the
v26 ledger (`85-GATE-4-SUMMARY.md`).

---

## 6. Citations

*The C1 identity (classical cubic-Jordan adjugate / cofactor).*
- N. Jacobson, *Structure and Representations of Jordan Algebras*, AMS Colloq. Publ. 39 (1968) — generic norm, adjoint, `(X#)# = N(X)X`.
- K. McCrimmon, *A Taste of Jordan Algebras*, Universitext, Springer (2004) — sharp/adjugate, cubic Jordan algebras.
- T. A. Springer & F. D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups*, Springer (2000); T. A. Springer, *Jahresber. DMV* (1962) on cubic forms.

*The canonical spectra.*
- A. Ikeda & Y. Taniguchi, "Spectra and eigenforms of the Laplacian on `S^n` and `P^n(C)`," Osaka J. Math. **15** (1978) 515–546 — `λ_j(CP^n) = 4j(j+n)`, so `λ_1(CP²) = 12`.
- R. S. Cahn & J. A. Wolf, "Zeta functions and their asymptotic expansions for compact symmetric spaces of rank one," Comment. Math. Helv. **51** (1976) 1–21 — CROSS spectra (incl. the Cayley plane `OP²`).
- A. L. Besse, *Manifolds all of whose Geodesics are Closed*, Ergeb. Math. 93, Springer (1978), ch. 3 / appendix — rank-one symmetric space spectra and normalizations.

*Two-point-homogeneous harmonic structure.*
- S. Helgason, *Groups and Geometric Analysis*, AMS (1984/2000); *Differential Geometry, Lie Groups, and Symmetric Spaces* — compact rank-one symmetric spaces are two-point homogeneous; multiplicity-free `L²`, the first spherical harmonic.

*Transitivity / the Cayley plane.*
- A. Borel, "Le plan projectif des octaves et les sphères comme espaces homogènes," C. R. Acad. Sci. Paris **230** (1950) — F₄ transitive on rank-1 idempotents, `OP² = F_4/Spin(9)`.
