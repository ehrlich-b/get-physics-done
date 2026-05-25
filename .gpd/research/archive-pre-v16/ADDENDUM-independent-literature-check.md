# Addendum: Independent Literature Check (2026-04-16)

**Source:** Parent conversation with Bryan Ehrlich (the project author), not produced by GPD scouts. Added before synthesizer spawned so this can be incorporated into SUMMARY.md.

**Purpose:** Narrow the search space for Phase 1. Two independent signals already strongly suggest that the V₁ vanishing lemma / Peirce preservation claim cannot be cited cleanly from A-S Ch. 7 (OUS level) and must instead be imported from JB-algebra (Jordan-level) sources. GPD should not waste cycles looking for an OUS-native citation that is not there.

## Finding 1: Alfsen-Shultz 2003 TOC analysis (subagent, 2026-04-16)

A subagent performed a TOC-level read of A-S 2003 via Springer metadata and Hanche-Olsen/Størmer cross-reference. Summary:

- **Ch. 7 "General Compressions"** — covers projections in cones, F-compressions, projective units, projective faces, geometry of projective faces. **No section named "Peirce decomposition."**
- **Ch. 8 "Spectral Theory"** — lattice of compressions, spaces in spectral duality, spectral convex sets. **No Peirce section.**
- **Ch. 9 "Characterization of Jordan Algebra State Spaces"** — Paper 5 cites "Theorem 9.37" for the Peirce direct sum. Chapter 9 is a Jordan-state-space characterization chapter, so invoking Theorem 9.37 at the pre-Jordan §3.3 level is circular.
- **Part I (Ch. 1-3)** — Peirce theory is developed here, entirely Jordan-algebraically.

Paper 5 cites A-S Prop 7.43 (facial absorption, correct, OUS-level) AND Theorem 9.37 (Peirce direct sum, incorrect for pre-Jordan use). Lean `SelfModelingBridge.lean` cites Prop 7.36 for a DIFFERENT step (S4 follow-through); these are two different claims, both citing unverified prop numbers.

Hanche-Olsen & Størmer *Jordan Operator Algebras* §2.6 develops Peirce decomposition **for unital Jordan algebras only**, using Macdonald's theorem. No OUS-level counterpart exists in that source either.

## Finding 2: Jenčová-Pulmannová arXiv:2102.01628 direct read (2026-04-16)

This 2021 paper **is the literature comparison paper for OUS spectrality approaches** (Alfsen-Shultz duality vs. Foulis compression bases). If Peirce decomposition existed at pure OUS level, this paper would develop it.

It does not.

Sections 3-4 (pages 4-21) develop OUS spectrality using: compressions, F-compressions, compression bases, projection cover property, comparability property, Mackey compatibility, C-blocks, Rickart mapping. **Peirce decomposition does not appear anywhere in these sections.**

**Peirce decomposition first appears in Section 5 "Spectrality for JB-algebras"**, specifically:

> **5.9 Theorem.** [3, Thm. 1.4] Let A be a **Jordan algebra** with unit 1, p ∈ A be a projection. Then A decomposes into the direct sum A = U_p(A) ⊕ U_{p,1-p}(A) ⊕ U_{1-p}(A), where [standard Peirce eigenspace definitions]. If x ∈ U_p(A) or x ∈ U_{1-p}(A) then x ∈ C(p).

The citation [3, Thm. 1.4] is A-S 2003 **Theorem 1.4**, Part I, Chapter 1 — the Jordan-algebraic Peirce chapter. Not Ch. 7.

**Jenčová-Pulmannová's own framing (Section 5 intro):** "We describe an important example of (spectral) compression bases on JB-algebras." Peirce structure enters only when JB-algebra structure is assumed.

## Implication for Phase 1

The claim "OUS + S1-S7 gives Peirce preservation" is NOT supported by the literature we can access. Two independent sources (A-S TOC + Jenčová-Pulmannová's comparison) locate Peirce decomposition post-Jordan, not pre-Jordan.

**Phase 1 outcome classification (prior probability update):**

- (A) Proof from OUS primitives: **plausible but difficult**. Would need to bypass Peirce entirely in proving S4, or find a non-Peirce characterization of the same claim. Worth a GPD attempt, but don't expect it.
- (B) A-S citation: **essentially ruled out**. No OUS-level A-S theorem exists. Any "citation fix" that lands on Ch. 1 or Ch. 9 is circular with respect to Paper 5's logical chain.
- (C) Structural gap: **most likely outcome**. The paper implicitly imports EJA-Peirce at a step where vdW has not yet been invoked. Resolution requires either:
  - (C-i) Adding a "Peirce coherence" axiom S0 alongside S1-S7, stated at OUS level, defended as natural.
  - (C-ii) Finding an alternative S4 proof that routes around Peirce entirely.
  - (C-iii) Restructuring the chain to derive Jordan structure before S4 — **this is not available** because vdW Thm 1 consumes S4 to produce Jordan structure; circularity.

**Recommendation for Phase 1 work:** Focus GPD effort on:
1. Attempting outcome (A) via a direct compression-algebra argument (J_p acts on Peirce subspaces as certified by A-S Ch. 7 compression theory, which is what we have). Cap the effort: if not found in reasonable time, shift to (C-i).
2. If (A) fails, formalize (C-i) — write the precise "Peirce coherence" axiom as it would appear at OUS level, and draft the paragraph Paper 5 would add to §3.3 stating and defending it.
3. Do NOT pursue (C-iii) unless a route around vdW Thm 1 is first demonstrated.

**References:**

- Alfsen & Shultz, *Geometry of State Spaces of Operator Algebras*, Birkhäuser 2003. TOC available via Springer/Deutsche Nationalbibliothek. Part I Ch. 1-3 (Jordan-algebraic Peirce), Ch. 7 (general compressions, no Peirce), Ch. 9 (Jordan state-space characterization, Theorem 9.37).
- Hanche-Olsen & Størmer, *Jordan Operator Algebras*, 1984. §2.6 Peirce decomposition, Jordan-only. Free PDF at hanche.folk.ntnu.no/joa/joa-m.pdf.
- Jenčová & Pulmannová, "Geometric and algebraic aspects of spectrality in order unit spaces: a comparison," arXiv:2102.01628, Feb 2021. Sections 3-4 OUS-level (no Peirce); Section 5.9 Peirce (Jordan-level, citing A-S Thm 1.4).
- van de Wetering, "Sequential Product Spaces are Jordan Algebras," arXiv:1803.11139. Theorem 1: S1-S7 ⇒ EJA. Consumes S4 to produce Jordan structure; cannot be inverted.
