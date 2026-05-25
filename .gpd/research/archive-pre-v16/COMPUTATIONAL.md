# Computational Approaches: Paper 5 Revision (v14.0) — Formalization and Numerical Sanity Infrastructure

**Surveyed:** 2026-04-16
**Domain:** Lean 4 proof engineering + small-case numerical/symbolic verification for operational-QM reconstruction (Alfsen-Shultz / van de Wetering)
**Confidence:** HIGH for Lean axiom tooling and SymPy sanity checks; MEDIUM for existing effect-algebra formalizations (none found upstream); HIGH for git/TeX revision workflow.
**Research mode:** balanced (per `.gpd/config.json`)

### Scope Boundary

COMPUTATIONAL.md covers computational TOOLS, libraries, and infrastructure for the six revision gaps (Phases 54–59). Mathematical proof strategy, theorem statements, and the physics content of what each axiom proves live in METHODS.md and PRIOR-WORK.md.

---

## Recommended Stack

Two small, mostly-independent toolchains:

1. **Lean 4 audit tooling** (Phase 58, dominant time sink): The existing `~/repos/research/lean` project (name: `RadicalRelativity`, Lean 4.28.0 pinned via `lean-toolchain`, mathlib `v4.28.0` via `lakefile.toml`) already contains the Paper 5 axioms as top-level `axiom` declarations with in-file docstring citations to Alfsen-Shultz chapters/propositions. Audit work is therefore: (a) programmatic extraction of every `axiom` declaration and every `#print axioms` dependency tail for each headline theorem, (b) one-to-one mapping to a cited source (Alfsen-Shultz, van de Wetering, or "flagged axiomatization"), (c) rebuild under pinned toolchain to confirm `0 sorry`. The native commands `#print axioms name` and a small Python post-processor over `lake build` output are sufficient; no new third-party tooling is strictly required. Optionally `lean-graph` (github.com/patrik-cihal/lean-graph) for a visual dependency graph to include in the revision response PDF.

2. **SymPy/NumPy finite-dimensional sanity checks** (Phases 54, 56): The smallest spectral OUS where the relevant claims are non-trivial is `H_3(R)` — 3×3 real symmetric matrices with the effect order `0 <= a <= 1` iff `0 <= lambda_i(a) <= 1` for every eigenvalue, compression `C_p(x) = p x p`, and sequential product `a o b = a^{1/2} b a^{1/2}`. This is small enough for exact SymPy computation on literal 3×3 matrices, and for NumPy spot-checks at random parameter values. Run time: seconds, not minutes. No HPC needed.

---

## Numerical Algorithms

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| `#print axioms` (Lean 4 built-in) | List every axiom a theorem transitively depends on | Exact (not iterative) | Linear in proof-term size | Proof term | Lean reference manual v4.25+ |
| `lake build` + error-code scan | Confirm `0 sorry`, no type errors under pinned toolchain | Terminating when no diagnostics | O(module size × elaboration cost) | ~1–3 GB per module for mathlib | Lake docs v5.0.0 |
| `sympy.Matrix.diagonalize()` | Spectral decomposition of 3×3 real symmetric matrix | Exact via characteristic polynomial (degree 3 closed form) | O(1) for fixed 3×3 | Negligible | SymPy 1.14 |
| `scipy.linalg.sqrtm` + `numpy.einsum` | Numerical sequential product `a^{1/2} b a^{1/2}` for random 3×3 effects | Backward stable to ~1e-12 for well-conditioned `a` | O(n^3) with small constant | O(n^2) | Higham, *Functional Matrices*, 2008 |
| `sympy.Matrix.eigenvects()` | Exact symbolic Peirce projections from orthogonal rank-1 spectral projectors | Exact when eigenvalues are distinct symbolic or rational | Polynomial in expression size | Bounded for 3×3 | SymPy docs |

### Convergence Properties

- **`#print axioms`:** deterministic, no convergence issue. Caveat: only reports axioms reachable through the *compiled* proof term. Declarations guarded by `sorry` will show `sorryAx` explicitly (verified behavior in Lean 4.25+; see lean-lang.org releases). The revision quality gate is: **no theorem cited in the paper prints `sorryAx` in its axiom list**, and every non-`Classical.choice`/`propext`/`Quot.sound` axiom in the list must be in the audit table with a published citation.
- **SymPy exact arithmetic:** zero floating-point error. Run time grows with expression complexity when symbols are kept unevaluated; for 3×3 matrices with 1–3 free parameters, each product evaluates in well under a second.
- **NumPy `scipy.linalg.sqrtm`:** principal square root; accurate for positive-definite matrices but loses precision as `a` approaches a rank-deficient effect (eigenvalues near 0 or 1). For the Peirce sanity check we construct `a` with strictly interior eigenvalues, so this is safe.

---

## Software Ecosystem

### Primary Tools

| Tool | Version | Purpose | License | Maturity |
|------|---------|---------|---------|----------|
| Lean 4 | `leanprover/lean4:v4.28.0` (pinned in `lean-toolchain`) | Check proof + extract axioms | Apache 2.0 | stable |
| mathlib | `v4.28.0` (pinned in `lakefile.toml` via `[[require]] name = "mathlib"`) | OUS/ordered-group/Jordan prerequisites | Apache 2.0 | stable |
| elan | 4.2.1 (installed at `~/.elan/bin/elan`) | Toolchain manager; respects `lean-toolchain` | Apache 2.0 | stable |
| Lake | 5.0.0 (bundled with Lean 4.28.0) | Build and script runner | Apache 2.0 | stable |
| Python | 3.11+ (sympy 1.14, numpy 2.4, scipy 1.17 already installed) | Post-processing Lean build output; sanity checks | PSF | stable |
| SymPy | 1.14.0 | Exact matrix arithmetic for Phase 54/56 | BSD | stable |
| NumPy | 2.4.2 | Floating-point spot checks, random-effect generation | BSD | stable |
| SciPy | 1.17.1 | `scipy.linalg.sqrtm` for numeric `a^{1/2}` | BSD | stable |
| Git + Git tags | any modern | `paper5-jmp-submitted` frozen tag already exists in `~/repos/blog` | GPL | stable |

### Supporting Tools

| Tool | Version | Purpose | When Needed |
|------|---------|---------|-------------|
| `latexdiff` | 1.3.x | Auto-diff `main-jmp-submitted.tex` vs `main.tex` for reviewer PDF | Phase 59 (reply to referee). **NOT installed on this machine** — user must `brew install --cask basictex && sudo tlmgr install latexdiff` or `brew install --cask mactex`. Flag before Phase 59 starts. |
| `git-latexdiff` | 1.6+ | Wraps `latexdiff` across git revisions, handles multi-file includes (this paper has `sections/*.tex`) | Phase 59, strongly preferred over raw `latexdiff` because Paper 5 uses `\input{sections/...}` |
| `lean-graph` | GitHub `patrik-cihal/lean-graph` | Theorem-dependency graph visualization, Lean 4 | **Optional** for Phase 58 — nice-to-have figure for referee; the audit itself does not need it |
| `lean-lsp-mcp` | Latest PyPI | Programmatic access to Lean LSP; could script axiom extraction | Optional; raw `#print axioms` via `lake env lean` is simpler |
| `jq` | any | Parse `lake-manifest.json` to pin/verify mathlib revision in the revision letter | Phase 59 reproducibility statement |

---

## Data Flow

```
Phase 58 (Lean axiom audit):
  ~/repos/research/lean/
    |-- lean-toolchain                    (pin: leanprover/lean4:v4.28.0)
    |-- lakefile.toml                     (pin: mathlib v4.28.0)
    |-- lake-manifest.json                (records resolved revisions)
    +-- RadicalRelativity/*.lean          (16-19 `axiom` decls, Paper 5 scope)
              |
              v
  `lake build` under pinned toolchain  -->  Build success + `0 sorry` confirmation
              |
              v
  AxiomAudit.lean  (new file; contains `#print axioms thm` for every paper-cited theorem)
              |
              v
  `lake env lean RadicalRelativity/AxiomAudit.lean > audit.txt`
              |
              v
  scripts/parse_axiom_audit.py  (simple regex parser over audit.txt)
              |
              v
  audit-table.md  -->  copied into `sections/axiom-verification.tex` or response-to-referee

Phase 54 (Peirce preservation sanity check):
  construct 3x3 spectral OUS in SymPy
              |
              v
  pick a = sum_i lambda_i p_i with distinct lambda_i in (0,1) and orthogonal rank-1 projectors
              |
              v
  loop over b in {V_2(p_i), V_1(p_i,p_j), V_0} basis
              |
              v
  compute a o b = a^{1/2} b a^{1/2}  (SymPy .sqrt or sum_i lambda_i^{1/2} p_i)
              |
              v
  assert resulting element stays in the same Peirce subspace (component norms off-subspace = 0)

Phase 56 (Thm 5.8 product-form on W):
  pick smallest W = anti-symmetric part of some real EJA embedding, e.g. 3-dim skew block
              |
              v
  compute sequential-product candidate on W and check product-form identity
              |
              v
  report symbolic result (confirms or falsifies paper claim for smallest case)
```

---

## Computation Order and Dependencies

| Step | Depends On | Produces | Can Parallelize? |
|------|-----------|----------|-----------------|
| 54a: set up `code/paper5_sanity.py` scaffolding (3×3 symmetric-matrix effect class, Peirce projections) | Python 3.11+, SymPy 1.14 | Reusable OUS helper | No (but fast) |
| 54b: Peirce preservation sanity check | 54a | Pass/fail table for 3 test `b`'s | Over b-choices, trivially |
| 56a: Construct smallest W and its candidate product | 54a (reuses spectral decomp utilities) | Symbolic expression for `a o_W b` | No |
| 56b: Verify product-form identity on W | 56a | Symbolic PASS/FAIL | No |
| 58a: Confirm `lake build` is green under pinned toolchain | elan + mathlib cache (or fresh `lake exe cache get`) | Build log, `0 sorry` certificate | No (single machine) |
| 58b: Write `RadicalRelativity/AxiomAudit.lean` with one `#print axioms` per paper-cited theorem | 58a, paper's theorem list | Audit text output | No |
| 58c: Parse audit output + map each axiom -> Alfsen-Shultz/vdW citation + flag "axiomatization-in-disguise" | 58b | `audit-table.md` | Per-axiom rows, trivially |
| 58d: Write Lean audit into `sections/axiom-verification.tex` | 58c | Paper-ready audit table | No |
| 59a: Generate `diff.pdf` via `git-latexdiff paper5-jmp-submitted main -- main.tex sections/` | 58d plus all Phase 54–58 paper edits | Reviewer-ready diff PDF | No |

**Critical ordering:** 58a before 58b (can't run `#print axioms` on a theorem that doesn't compile). 58c before 58d (audit table needs the mapping). 59a strictly last.

---

## Resource Estimates

| Computation | Time (estimate) | Memory | Storage | Hardware |
|-------------|-----------------|--------|---------|----------|
| Fresh `lake exe cache get` for mathlib v4.28.0 | 2–10 min (network-bound, ~3 GB of oleans) | ~2 GB peak | ~4 GB on disk | Laptop, stable internet |
| `lake build` from clean (no cache) under pinned toolchain | 30–90 min on Apple Silicon laptop; 5–15 min with cache | 4–8 GB peak | N/A additional | Laptop |
| `lake build` incremental after cache | <2 min for edits local to `RadicalRelativity/*.lean` | ~2 GB | N/A | Laptop |
| Writing `AxiomAudit.lean` with ~20–40 `#print axioms` lines | 30–60 min human time | Trivial | ~5 KB | Editor |
| Running `AxiomAudit.lean` and parsing output | <30 s | Trivial | ~20 KB audit.txt | Laptop |
| **Human review:** map each printed axiom to Alfsen-Shultz/vdW citation, verify statement matches, classify as "cited" vs "axiomatization-in-disguise" | **6–12 hours for 16–19 axioms** (30–45 min per axiom: locate printed statement, find page in Alfsen-Shultz, confirm signature matches, decide verdict) | — | — | Human + PDF reader |
| Write `sections/axiom-verification.tex` | 2–4 hours | — | — | Editor |
| Phase 54 Peirce sanity check (implement + test) | 2–3 hours | <100 MB | <10 KB | Laptop |
| Phase 56 smallest-W computation (symbolic) | 1–2 hours + some debugging | <100 MB | <10 KB | Laptop |
| `git-latexdiff` run + manual cleanup of broken diff in equations | 1–3 hours (diffs in math mode often need hand-tuning) | Trivial | ~5 MB for diff PDF | Laptop + TeX Live |
| **Total Phase 54** | ~3 hours (sanity check is small) | — | — | — |
| **Total Phase 56** | ~2 hours | — | — | — |
| **Total Phase 58 (dominant)** | **1.5–2 working days** (1 day if only 16 axioms are clean cites, 2 days if some need re-statement in terms that match a published theorem) | — | — | — |
| **Total Phase 59** | ~4 hours (diff + response letter formatting) | — | — | — |

**Honest total across Phases 54–59:** 3–4 working days if everything goes smoothly; 5–7 days with realistic debugging and at least one "oh no, this axiom doesn't actually appear in Alfsen-Shultz Ch. 9, it's in Hanche-Olsen-Stormer Ch. 3" discovery. Phase 58 is by far the largest.

---

## Integration with Existing Code

- **Input formats:**
  - Lean side: `.lean` source files already on disk in `~/repos/research/lean/RadicalRelativity/`. The project is name `RadicalRelativity` (not `Paper5` — verified). 19 top-level `axiom` declarations across the project; Paper 5 scope is primarily `SelfModelingBridge.lean` (13 axioms), `CStarBridge.lean` (1 axiom: `vdw_theorem_3`), `NonComposability.lean` (4 axioms including JvNW classification and Hanche-Olsen), and 1 in `ObserverInterface.lean`. The **16-count in the milestone context** matches after filtering to Paper 5 scope and excluding the 3 `NonComposability` axioms that are Paper-6-specific; the Phase 58 plan should first *confirm which 16*.
  - Python side: no existing Paper 5 code in the working tree. Create `code/paper5_sanity.py` as a new file. `code/octonion_algebra.py` is Paper-6-specific and does NOT share structure with spectral OUS on `H_3(R)`; do not try to reuse.

- **Output formats:**
  - Phase 58 produces plain Markdown `audit-table.md` that gets transcluded or manually copied into `sections/axiom-verification.tex`. The TeX section already exists (`sections/axiom-verification.tex` was in the JMP submission), so the audit table replaces/augments existing content.
  - Phase 54/56 sanity checks produce pass/fail log + short `.txt` report suitable for inclusion in `sections/appendix-numerical.tex` if the reviewer asks for more evidence.

- **Interface points:**
  - `~/repos/research/lean/RadicalRelativity/AxiomAudit.lean` — new file, imports all Paper-5-relevant modules, contains `#print axioms` lines. Does not affect the existing proof; purely informational.
  - `code/paper5_sanity.py` — new, standalone.
  - `sections/axiom-verification.tex` — existing file in the paper; edited in Phase 58d.

---

## Validation Strategy

| Result | Validation Method | Benchmark | Source |
|--------|------------------|-----------|--------|
| `lake build` succeeds under pinned toolchain | `cd ~/repos/research/lean && lake build 2>&1 \| tee build.log`; grep for `sorry\|error` | Zero `error`, zero `sorry` lines | Existing project claim + lake docs |
| Axiom count matches | `grep -rn "^axiom" RadicalRelativity/*.lean \| wc -l` plus paper-scope filter | 16 (per milestone context); audit if differs | Direct file scan (result: 19 total, user claims 16 Paper-5-specific — reconcile in Phase 58 first step) |
| Every paper-cited theorem's `#print axioms` contains only: `propext`, `Classical.choice`, `Quot.sound`, plus enumerated published-result axioms | Inspection of `audit.txt` | No `sorryAx` appears anywhere | Lean reference manual |
| Spectral decomposition test on H_3(R) | Construct `a = 0.2 * p_1 + 0.5 * p_2 + 0.3 * p_3` with random orthogonal rank-1 `p_i`; recover eigenvalues via `Matrix.diagonalize()` | Eigenvalues match {0.2, 0.5, 0.3} to exact (SymPy) or 1e-12 (NumPy) | Alfsen-Shultz Thm 9.33 |
| Sequential product symmetry test | `a o a = a^2` should hold for any effect `a` | Exact match in SymPy for `H_3(R)` entries | Gudder-Greechie 2002, sequential-product axioms |
| Peirce preservation on concrete example | For orthogonal rank-1 `p, q` in `H_3(R)`, compute `V_2(p)`, `V_1(p,q)`, `V_0` via `C_p(x) = pxp`, `(pxq+qxp)`, `(I-p-q)x(I-p-q)`; verify `a o b` for `a = alpha p + beta q + gamma (I-p-q)` maps `V_j(p) -> V_j(p)` | Off-diagonal entries equal zero to machine precision | Alfsen-Shultz Ch. 7, Peirce decomposition |
| `git-latexdiff paper5-jmp-submitted HEAD -- main.tex` produces valid PDF | Visual inspection + `pdftotext` round-trip | No lost paragraphs, equations readable | Timothy Gebhard's blog (git-latexdiff for rebuttals) |

---

## Concrete Commands and Code Snippets

### Phase 58: Lean axiom audit commands

```bash
# 1. Verify pinned toolchain is present (elan auto-installs from lean-toolchain on first use)
cd ~/repos/research/lean
cat lean-toolchain       # must read: leanprover/lean4:v4.28.0

# 2. Pull mathlib binary cache (saves 30-90 min of compile time)
lake exe cache get       # downloads ~3 GB of compiled .olean files

# 3. Build everything; must be green before audit
lake build 2>&1 | tee build.log

# 4. Confirm zero sorry
grep -rn "sorry" RadicalRelativity/ || echo "CLEAN: zero sorry"

# 5. List axioms in source (structural count)
grep -n "^axiom " RadicalRelativity/*.lean

# 6. Write the audit file (new file; see template below)
#    Then run:
lake env lean RadicalRelativity/AxiomAudit.lean > audit.txt 2>&1

# 7. Record exact mathlib revision used (for revision letter reproducibility)
jq '.packages[] | select(.name=="mathlib") | .rev' lake-manifest.json
```

### `RadicalRelativity/AxiomAudit.lean` template

```lean
-- Phase 58 audit: for each headline theorem cited in Paper 5,
-- emit the transitive axiom list. This file is build-informational
-- only; its output goes into the revision response to the referee.

import RadicalRelativity.SelfModelingBridge
import RadicalRelativity.CStarBridge
import RadicalRelativity.SequentialProduct
import RadicalRelativity.OrderUnitSpace
-- (import any module whose headline theorem is cited in the paper)

namespace AxiomAudit

-- One #print axioms per headline theorem. Replace with actual theorem names.
#print axioms SelfModelingBridge.selfModelProduct_well_defined
#print axioms SelfModelingBridge.self_modeling_locally_tomographic
#print axioms CStarBridge.self_modeling_to_c_star
-- ... etc, one line per headline claim cited in main.tex

end AxiomAudit
```

Expected output format (sample, per Lean 4 reference manual):

```
'SelfModelingBridge.self_modeling_locally_tomographic' depends on axioms:
  [propext, Classical.choice, Quot.sound,
   SelfModelingBridge.has_compression,
   SelfModelingBridge.has_spectral_decomp,
   SelfModelingBridge.spectral_reconstruct,
   SelfModelingBridge.diagonal_peirce_vanish,
   SelfModelingBridge.compress_annihilates_peirce1,
   SelfModelingBridge.peirce1_annihilates_compress,
   SelfModelingBridge.peirce1_orthogonal_idem,
   SelfModelingBridge.compress_orthogonal_product,
   SelfModelingBridge.selfModelProduct_nonneg,
   SelfModelingBridge.compatibility_iff_peirce_vanish,
   SelfModelingBridge.compatible_peirce_sp_commute,
   SelfModelingBridge.orthogonal_face_sp_zero,
   SelfModelingBridge.compatible_simultaneous_decomp,
   SelfModelingBridge.selfModelProduct_any_decomp,
   SelfModelingBridge.self_modeling_locally_tomographic]
```

The three baseline axioms (`propext`, `Classical.choice`, `Quot.sound`) are Lean's built-in classical-logic axioms and are *not* Paper-5-specific; all other listed identifiers are project axioms that need an audit-table row.

### Audit table format (goes into `sections/axiom-verification.tex`)

For each non-builtin axiom, Phase 58 produces one row:

| Axiom | Stated in | Verdict | Citation | Lean-statement matches citation? |
|---|---|---|---|---|
| `has_compression` | `SelfModelingBridge.lean:211` | Cited | Alfsen-Shultz 2003, Ch. 9 (existence of compressions in spectral OUS) | YES / NEEDS WORK / AXIOMATIZATION |
| `spectral_reconstruct` | `SelfModelingBridge.lean:220` | Cited | Alfsen-Shultz 2003, Thm 9.33 | YES |
| ... | ... | ... | ... | ... |
| `vdw_theorem_3` | `CStarBridge.lean:83` | Cited | van de Wetering 2019, Thm 3 (effect-theoretic reconstruction) | YES |

**Verdict classes (mutually exclusive):**
- **Cited** — axiom is a direct transcription of a published theorem, signature matches.
- **Axiomatization-in-disguise** — axiom is *our* load-bearing assumption that is NOT a published theorem. Must either be (a) promoted to a theorem and proven, or (b) stated explicitly as an axiom of *this paper* with physical justification. This category must be flagged to the referee honestly.
- **Signature mismatch** — axiom claims more than the published theorem gives. Action: weaken the axiom to match or promote to a proof.

**Note on already-in-file citations:** Inspection of `SelfModelingBridge.lean` (lines 204–280) shows the axioms are *already* docstring-commented with Alfsen-Shultz references (e.g., "Alfsen-Shultz 2003, Thm 9.33", "Alfsen-Shultz 2003, Prop 7.48", "Alfsen-Shultz 2003, Chapter 7"). The Phase 58 job is to **verify those citations are accurate** (signature matches the published theorem), not to invent them from scratch. This cuts Phase 58 time roughly in half relative to a cold audit.

### Phase 54: Peirce preservation SymPy/NumPy snippet

```python
# code/paper5_sanity.py
"""Smallest-case sanity check: spectral product a o b preserves Peirce subspaces
on H_3(R), the 3x3 real symmetric matrices with effect order.

This is a finite-dimensional spot check, NOT a proof. Its role is to verify the
claim holds numerically on the smallest nontrivial example, which catches any
sign/factor-of-2 error in the paper's statement before the Lean formalization
phase."""

import numpy as np
from scipy.linalg import sqrtm

def random_spectral_effect_3x3(seed=0):
    """Return (a, [p1,p2,p3], [lam1,lam2,lam3]) where a = sum lam_i p_i,
    the p_i are orthogonal rank-1 projectors from a random orthonormal basis,
    and lam_i are distinct values in (0,1)."""
    rng = np.random.default_rng(seed)
    Q, _ = np.linalg.qr(rng.standard_normal((3,3)))       # random orthogonal 3x3
    projs = [np.outer(Q[:,i], Q[:,i]) for i in range(3)]   # rank-1 p_i
    lams  = [0.2, 0.5, 0.7]                                # distinct, interior
    a = sum(l * p for l, p in zip(lams, projs))
    return a, projs, lams

def compress(p, x):
    """C_p(x) = p x p -- the compression map on H_n(R)."""
    return p @ x @ p

def V1_op(Pi, Pj, x):
    """Peirce V_1(p_i, p_j)-component of x: (p_i + p_j) x (p_i + p_j) - C_pi(x) - C_pj(x)."""
    S = Pi + Pj
    return S @ x @ S - compress(Pi, x) - compress(Pj, x)

def seq_product(a, b):
    """a o b = a^{1/2} b a^{1/2} (numerical)."""
    a_sqrt = sqrtm(a).real    # a is PSD; take real part to kill FP noise
    return a_sqrt @ b @ a_sqrt

def test_peirce_preservation():
    a, projs, lams = random_spectral_effect_3x3(seed=42)
    p, q, r = projs
    I3 = np.eye(3)

    # Random symmetric test element X
    rng = np.random.default_rng(7)
    X = rng.standard_normal((3,3))
    X = (X + X.T) / 2

    # Test 1: b in V_2(p). a o b should remain in V_2(p).
    b = compress(p, X)
    aob = seq_product(a, b)
    residual = (I3 - p) @ aob @ (I3 - p)
    assert np.linalg.norm(residual) < 1e-10, (
        f"FAIL V_2(p): residual={np.linalg.norm(residual):.2e}"
    )
    print(f"PASS: a o V_2(p) subset V_2(p)  (residual {np.linalg.norm(residual):.2e})")

    # Test 2: b in V_1(p,q).
    b = V1_op(p, q, X)
    aob = seq_product(a, b)
    # a o b should be in V_1(p,q); check projection to V_2(p) cap V_2(q) cap V_0 is small
    # (simplest: check compress(r, aob) which would be in V_2(r) -- should vanish)
    residual = compress(r, aob)
    assert np.linalg.norm(residual) < 1e-10, (
        f"FAIL V_1(p,q): leak into V_2(r), residual={np.linalg.norm(residual):.2e}"
    )
    print(f"PASS: a o V_1(p,q) subset V_2(p)+V_1(p,q)+V_2(q)  (V_2(r) residual {np.linalg.norm(residual):.2e})")

    # Test 3: a o a = a^2
    aoa = seq_product(a, a)
    assert np.linalg.norm(aoa - a @ a) < 1e-10, "FAIL: a o a != a^2"
    print(f"PASS: a o a == a^2  (residual {np.linalg.norm(aoa - a@a):.2e})")

if __name__ == "__main__":
    test_peirce_preservation()
```

Expected run time: **<1 second**. If it fails, the paper's Peirce-preservation claim is wrong *before* we ever touch Lean.

**NOTE on `a o b` definition:** The paper's sequential product is the one defined in `SelfModelingBridge.lean` (the "self-modeling product"), which for special EJAs reduces to `a^{1/2} b a^{1/2}`. For `H_3(R)` with the standard spectral structure this reduction is exact; the sanity check is valid there. For non-JB-algebra OUS the paper's product differs and this sanity check does *not* apply — Phase 54 should be scoped to `H_3(R)` as the confirming example, not a general test.

### Phase 56: smallest-W product-form check

```python
# code/paper5_thm58.py
"""Smallest-case check of Theorem 5.8: W carries a product-form sequential product.

'Product-form' in the paper means: there exist fixed matrices L, R such that
a o_W b = L a L^* b R R^* for all a, b in W, i.e., the product factors through
left/right multiplication by fixed elements. Here we instantiate W as the
3-dim antisymmetric block of a real EJA and check whether the candidate product
satisfies this identity symbolically."""

import sympy as sp

def smallest_W_basis():
    """Symbolic basis for the 3-dim antisymmetric part of M_3(R), viewed as the
    'wedge' component in an H_3(R)-like spectral OUS."""
    E12 = sp.Matrix([[0,1,0],[-1,0,0],[0,0,0]])
    E13 = sp.Matrix([[0,0,1],[0,0,0],[-1,0,0]])
    E23 = sp.Matrix([[0,0,0],[0,0,1],[0,-1,0]])
    return [E12, E13, E23]

def check_product_form():
    basis = smallest_W_basis()
    a, b = basis[0], basis[1]
    # Candidate 1: Jordan product (1/2)(ab+ba) -- on antisymmetric blocks this
    # is symmetric, NOT in W, so "product-form on W" for this product is vacuous.
    jordan = sp.Rational(1,2) * (a*b + b*a)
    print("(a o b) via Jordan product:")
    sp.pprint(jordan)
    # Candidate 2: the paper's W-product (fill in once Thm 5.8 statement is extracted).
    # Placeholder:
    # L, R = ... (fixed matrices from paper)
    # W_prod = L @ a @ L.T @ b @ R @ R.T
    # return sp.simplify(W_prod - expected_form)

if __name__ == "__main__":
    check_product_form()
```

This snippet is a **starting point**; the *exact* product-form identity to check depends on the paper's Thm 5.8 statement, which the phase planner should extract from `main.tex` and encode precisely before running. Paper 5's current text may need to be re-read carefully to get the identity right — flag as a minor risk.

### Phase 59: revision diff workflow

```bash
# Prerequisite: install latexdiff (NOT CURRENTLY INSTALLED on this machine)
# Option 1: BasicTeX (small)
brew install --cask basictex
sudo tlmgr update --self
sudo tlmgr install latexdiff
# Option 2: full MacTeX (larger, but one-shot)
brew install --cask mactex

# Also install git-latexdiff (handles \input{sections/...} properly)
brew install git-latexdiff    # or: pipx install git-latexdiff
# If not in Homebrew, fallback: git clone https://gitlab.com/git-latexdiff/git-latexdiff

# From inside ~/repos/blog/landing/papers/qm-from-self-modeling:
cd ~/repos/blog/landing/papers/qm-from-self-modeling
git-latexdiff paper5-jmp-submitted HEAD --main main.tex --output diff.pdf \
  --exclude-textcmd="section,subsection,subsubsection"

# Also record the Lean toolchain in the revision letter's reproducibility section:
LEAN_VER=$(cat ~/repos/research/lean/lean-toolchain)
MATHLIB_REV=$(jq -r '.packages[] | select(.name=="mathlib") | .rev' \
               ~/repos/research/lean/lake-manifest.json)
echo "Lean: $LEAN_VER"
echo "mathlib revision: $MATHLIB_REV"
```

**Caveat:** `latexdiff` often produces broken output in align environments and `\newcommand`-heavy files. Budget 1–3 hours of hand-tuning after the first run. The Crosetto `reply_to_referee_template` and the Zenke Lab template give structural patterns for the response-to-referee document; use Crosetto's as the base for `response.tex`.

---

## Anti-Approaches (things NOT to do)

| Anti-approach | Why avoid | What to do instead |
|---|---|---|
| Write a Python script that parses `.lean` source for `axiom` declarations and assumes that's the full audit | Misses axioms added indirectly via `import mathlib` and via definitions that bake in `Classical.choice`. Only `#print axioms` is authoritative. | Use `#print axioms` per headline theorem, accept the 3 Lean builtins, audit the rest. |
| Skip `lake exe cache get` and compile mathlib from scratch | Costs 30–90 min on first run; the cache is the community-standard workflow | Always run `lake exe cache get` right after `git pull` or first clone. |
| Unpin the toolchain during revision ("let's upgrade to Lean 4.29 while we're here") | Any upgrade risks breaking proofs and invalidates the "16 axioms, 0 sorry" claim | Keep `lean-toolchain` exactly as submitted for JMP. Only upgrade in a separate, post-acceptance milestone. |
| Try to reuse `code/octonion_algebra.py` for Paper 5 sanity checks | It's Paper-6 scope (Albert algebra / h_3(O) / exceptional Jordan), wrong algebra class entirely | Write `code/paper5_sanity.py` fresh; ~100 lines. |
| Run Phase 58 without first confirming `lake build` is green | `#print axioms` on a stale or broken project gives misleading output | 58a is strict prerequisite to 58b. |
| Use `latexdiff main-jmp-submitted.tex main.tex` directly | Misses changes in `sections/*.tex`; Paper 5 uses `\input{sections/appendix-proofs}` etc. | Use `git-latexdiff` with the frozen tag `paper5-jmp-submitted`. |
| Over-engineer a CI pipeline for the axiom audit | One-shot revision task; lifetime ~2 weeks; CI overhead not justified | Manual `lake env lean RadicalRelativity/AxiomAudit.lean` is fine. |
| Hand-extract axiom statements into LaTeX without re-running `#print axioms` after each edit | Edits to a proof can silently *add* dependencies (e.g., a new `sorry`-guarded helper) | After every non-trivial proof edit in Phase 58–59, re-run the audit. |

---

## Open Questions (for phase planners to resolve)

| Question | Why open | Impact |
|---|---|---|
| Is the "16 axioms" count correct, or is it 19 (all top-level `axiom` decls in the project) minus Paper-6-specific ones (e.g., `NonComposability` and `ObserverInterface`)? | User states 16 in milestone context but grep finds 19 in Paper-5-relevant modules | Phase 58 first step must reconcile: run `#print axioms` on the *paper's cited theorems only* (not every module), count the distinct non-builtin axioms that appear |
| Does mathlib v4.28.0 actually provide `OrderUnitSpace` or is it a project-local definition? | Search did not surface a mathlib `OrderUnitSpace` structure; `RadicalRelativity/OrderUnitSpace.lean` exists in the project | If project-local (likely), the audit should note this and cite the project file rather than mathlib |
| Is there a published Lean 4 formalization of effect algebras or spectral OUS that we should cite as prior art? | Searches (mathlib4, Tobias Fritz, ACT 2019) returned nothing dedicated | Likely safe to state "no prior Lean formalization of Alfsen-Shultz-type spectral OUS exists"; the reviewer may find this a selling point |
| For Phase 56, what is the *exact* identity "W carries a product-form sequential product" the paper claims? | Sanity check depends on knowing the exact formula | Phase planner must extract from `main.tex` Thm 5.8 statement before writing the SymPy check |
| Which specific theorems in `main.tex` are the "headline" theorems whose `#print axioms` trace we care about for the referee? | Paper has many lemmas; the audit should target the main theorems only | Extract from the paper's theorem environments marked \begin{theorem}; likely 5–10 headline theorems |

---

## Key References

- **Lean 4 `#print axioms` semantics** — Theorem Proving in Lean 4, Ch. 12 (Axioms and Computation): https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/
- **Lean 4.25 release notes (sorryAx behavior)** — https://lean-lang.org/doc/reference/latest/releases/v4.25.0/
- **Lake build system + scripting** — https://lean-lang.org/doc/reference/latest/Build-Tools-and-Distribution/Lake/
- **mathlib4** (pinning, cache) — https://github.com/leanprover-community/mathlib4
- **lean-graph** (optional dependency-graph visualization) — https://github.com/patrik-cihal/lean-graph
- **van de Wetering, "An effect-theoretic reconstruction of quantum theory"** — arXiv:1801.05798, *Compositionality* 1:1 (2019). Gives Thm 3 (effect-theoretic reconstruction into finite-dim C*) — source for `vdw_theorem_3` axiom.
- **van de Wetering, "On the properties of spectral effect algebras"** — https://quantum-journal.org/papers/q-2019-06-03-148/ — background for spectral-OUS reasoning.
- **Alfsen-Shultz, "State Spaces of Operator Algebras"** (Birkhäuser 2001/2003) — ISBN 978-0817638900 — primary source cited by 13 of the 16 Paper 5 axioms.
- **Hanche-Olsen & Størmer, "Jordan Operator Algebras"** — Pitman 1984 — secondary source for `hanche_olsen_composite` axiom (Paper-6 scope; verify whether needed for Paper 5).
- **Timothy Gebhard, "Using git-latexdiff for paper rebuttals"** — https://timothygebhard.de/posts/using-git-latexdiff-for-paper-rebuttals/ — concrete workflow.
- **Paolo Crosetto, `reply_to_referee_template`** — https://github.com/paolocrosetto/reply_to_referee_template — response letter structure with latexdiff integration.
- **Zenke Lab LaTeX rebuttal template** — https://zenkelab.org/resources/latex-rebuttal-response-to-reviewers-template/ — alternate template with color-coded changes.
- **Higham, N. J., *Functions of Matrices: Theory and Computation*, SIAM, 2008** — reference for numerical `sqrtm` stability.

## Sources

- [Lean `#print axioms` notes (Zucker blog)](https://www.philipzucker.com/notes/Languages/lean/)
- [Theorem Proving in Lean 4 — Axioms and Computation](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/)
- [Lean 4.25.0 release notes](https://lean-lang.org/doc/reference/latest/releases/v4.25.0/)
- [mathlib4 repository](https://github.com/leanprover-community/mathlib4)
- [lean-graph — dependency graph extractor for Lean 4](https://github.com/patrik-cihal/lean-graph)
- [Lean-auto (ATP interface; context on Lean tooling)](https://arxiv.org/html/2505.14929)
- [LeanExplore search engine](https://arxiv.org/html/2506.11085v1)
- [van de Wetering, effect-theoretic reconstruction (arXiv:1801.05798)](https://arxiv.org/abs/1801.05798)
- [van de Wetering, Compositionality 2019 (open-access)](https://compositionality.episciences.org/13504)
- [On the properties of spectral effect algebras (Quantum 2019)](https://quantum-journal.org/papers/q-2019-06-03-148/)
- [Spectral resolutions in effect algebras (Quantum 2022)](https://quantum-journal.org/papers/q-2022-11-03-849/)
- [Alfsen-Shultz, State Spaces of Operator Algebras — bibliographic](https://www.amazon.com/State-Spaces-Operator-Algebras-Orientations/dp/0817638903)
- [Timothy Gebhard — git-latexdiff for rebuttals](https://timothygebhard.de/posts/using-git-latexdiff-for-paper-rebuttals/)
- [Crosetto `reply_to_referee_template`](https://github.com/paolocrosetto/reply_to_referee_template)
- [Zenke Lab rebuttal template](https://zenkelab.org/resources/latex-rebuttal-response-to-reviewers-template/)
- [SymPy 1.14 matrix documentation](https://docs.sympy.org/latest/modules/matrices/matrices.html)
