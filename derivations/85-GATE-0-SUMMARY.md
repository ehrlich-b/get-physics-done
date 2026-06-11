# 85 — GATE 0 SUMMARY: frames + machinery (fail-fast)

**v25.0 Phase 85. Exact over Q / Q(t). ALL PASS.** Driver `code/variety_moment_doublet.py`.

The machinery the verdicts rest on, certified before any claim is tested.

- **0.a sharp `X#` pinned to the repo conventions** (the convention-drift guard). `X#`
  is built only from `RL.jordan/Tr/identity` as `X∘X − Tr(X)X + σ₂(X)I` and verified by
  its three classical defining identities, exactly:
  - `(X#)# == det_3(X)·X` (adjugate identity);
  - `Tr(X#∘Y) == ½·d(X,X,Y)` (`X#` = gradient of the cubic norm `N`, `d = RL.polarize_d`);
  - `Tr(X#) == σ₂(X)`; and rank-1 `E_11# == 0`, `Tr E_11 == 1`.
  *(This gate caught a real bug in the first driver build — a misnamed `I/3`-vs-`I`
  in the sharp formula — before any verdict was read. The guard works.)*

- **0.b 16-family battery** `(j,k)`, `j∈{1,2}, k∈0..7`, exact over Q(t): each family
  `p∘p = p`, `Tr p = 1`, `p(0) = E_11`, and passes the **c11-form certificate**
  `c11(t) = Tr(p∘E_11) == ((1−t²)/(1+t²))²` (unit-speed canonical geodesic). All 16
  survive. The **CP² cut** = the 4 c11-certified families landing in the bottleneck
  tangent `{11,18,19,26}`: `(1,0)→19, (1,7)→26, (2,0)→11, (2,7)→18`. (The "missing"
  v24 cut family was `(2,7)→slot 18`; built here. Note: the prompt's parenthetical
  "coord 26" for the missing family is `(1,7)`, which already existed; the 4-frame is
  completed by `(2,7)→18`.)

- **0.c orthonormal tangent frame.** The 16 tangents `e_i = p_i'(0)` have trace-form
  Gram `= 8·I_16` (orthogonal, equinormed) ⇒ `{e_i/√8}` is an orthonormal frame; the
  canonical (Spin(9)-invariant) metric on `V_{1/2}(E_11)` is the trace form up to this
  global scale, fixed to unit speed by the c11 certificate.

- **0.d Laplacian assembler.** `Δf(E_11) = Σ_i (f∘γ_i)''_θ(0)` over the orthonormal
  geodesic frame; the chain rule `t = tan(θ/2)` gives `dt/dθ|_0 = 1/2`,
  `d²t/dθ²|_0 = 0`, so `f''_θ(0) = ¼ f''_t(0)`. Verified on `c11 = cos²θ`:
  `¼·c11''_t(0) = ¼·(−8) = −2 = (cos²θ)''_θ(0)` per direction.

**Gate 0: ALL PASS** — sharp certified, 16 + 4 frames c11-certified and orthonormal,
Laplacian assembler validated.
