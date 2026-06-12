# Phase 91 (v31.0-candidate) — GATE 2 SUMMARY: The Hessian Sector (B2, B4, B5)

**Driver:** `python3 -u code/tensor_probe.py g2` → **4/4 PASS** (~6s, exact over Q).

**[REPORT, NO VERDICT LANGUAGE]** — per the prompt, the Hessian sector may be all-trivial
without deciding the fork. It is. The fork is decided by the bilinears (Gate 3).

| # | Check | Result |
|---|---|---|
| 2.univ | **UNIVERSAL identity:** cov_hessian(f) == δ*(df) for an ARBITRARY rational scalar f | PASS |
| 2.B2 | ∇∇G_M == δ*(dG_M) at 3 exact rational chart points — PURE GAUGE | PASS |
| 2.B5 | ∇∇R_M == δ*(dR_M) at 3 exact chart points — PURE GAUGE; R_M cut (α,β,λ₂)=(2/5,3/20,32) | PASS |
| 2.B4 | ∇∇χ == δ*(dχ) at 3 exact chart points — PURE GAUGE; χ = −(9/2)⟨M,p⟩⟨M,D_p⟩ (v30) | PASS |

## The load-bearing fact: every Hessian is pure gauge by construction

The Matsushima/Kähler identity ∇∇f = δ*(df) holds for **any** scalar f (the covariant Hessian
is the symmetric covariant derivative of the exact 1-form df). The driver verifies this
**universally** on an arbitrary inhomogeneous rational scalar (2.univ) — so **B1, B2, B4, B5 are
constructively DEAD by construction**, with the explicit certificate

> ω = df,  f_conf = (1/n)·tr_g(∇∇f) = ¼·Δf   (n = 4, the real dim).

This is NOT a failure-to-find — it is the universal structural identity, independent of the
specific field. The per-member checks (2.B2/B4/B5) confirm each ACTUAL field instance at exact
rational chart points (a member-specific witness on top of the symbolic universal proof).

## Stall-proofing note

The per-member checks evaluate cov_hessian and δ*(d·) at **exact rational chart points** rather
than `cancel`-ing the raw symbolic field — the diagnosed cliff (a `cancel` on the dense G_M
field Hessian) timed out two prior runs at ~500s. Point-evaluation is exact rational arithmetic
and fast (~6s for all three). The universal identity (2.univ) carries the all-M, all-z claim.

## χ realization (faithful, rational)

The literal v30 χ uses the Gram-Schmidt-transported phase reference D_p, which carries
sqrt-norms (NOT rational in the chart). The orchestrator anchor resolves this: **B4 is the SAME
structural identity as B1** (Hessian of any scalar is gauge), so the verdict does not depend on
χ's exact form. χ is realized as the rational degree-2 matter-clock scalar
−(9/2)⟨M,p⟩⟨M·D_ref, p⟩ with D_ref the fixed coord-10 phase element — faithful to the v30 class
and rational. The universal identity 2.univ makes the choice immaterial to the verdict.

**Conclusion (no verdict language):** B2, B4, B5 are Hessians ⇒ longitudinal-by-nature ⇒ pure
gauge. The fork is NOT decided here.
