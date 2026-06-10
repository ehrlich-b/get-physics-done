# Slot 83 / v23.0-candidate — GATE 1 SUMMARY (calibration)

**The Two-Term Balance Question (Jacobson J5, fiber side) — Gate 1: confirm X = I/3 is the
unconstrained fixed-trace maximum of S_face.** The pre-registered §8.1 tautology — **MUST
pass, carries ZERO evidence**. Status: **PASS.**

Exact over Q (log symbolic), source-guarded. Driver: `code/entanglement_two_term.py`
`gate1()`.

---

## What was checked (rank-2 meaningful face; rank-1 is trivial S ≡ 0)

Expanded `S_face^{(rank2)}(I/3 + εH)` to O(ε²) for a **general 27-dim** perturbation `H`,
exact over Q. The face-eigenvalue degeneracy at I/3 (corner eigenvalues coincide at 1/3)
makes the entropy non-analytic; handled by the `ε > 0` series (the ε² Fisher coefficient
simplifies to a genuine polynomial — residual `√` pieces cancel, verified).

| check | result |
|-------|--------|
| `S_face(I/3)` | **log 2** (rank-2; rank-1 face trivial S ≡ 0) |
| `δS_face` in all 27 tangent directions | **0** (identically, as a polynomial in `h_0…h_26`) |
| S_face support | only the face block `{1..10}`; `{0}` and `{11..26}` absent ⇒ δ = 0 there trivially |
| face Hessian (10×10) eigenvalues | `{ 0 (×1), −9/2 (×1), −9 (×8) }` — **negative-semidefinite ⇒ I/3 is the MAX** |
| the single zero eigenvalue | the scale-invariant face-trace `(β+γ)` direction |

The Fisher form: `δ²S_face = (9/4)·[ −(h_β − h_γ)² − 4(h_3²+…+h_10²) ]` — negative-definite
on the 9 traceless face directions (`−9/2` on β−γ, `−9` on each x1-octonion dir); flat on
the scale direction (β+γ).

## Reading

`δS_face = 0` in all 27 directions ⇒ I/3 is a critical point of S_face; the Hessian
negative-semidefiniteness ⇒ it is the **maximum**. This is the §8.1 degeneracy
(`K = (log 3)·I`, first variations vanish). **Gate 1 PASS ⇒ the setup is sound.**

Per the pre-registration, passing this proves **NOTHING** about the route — the one-term
entropy extremum IS the tautology this run exists to go beyond. The evidential question is
Gate 2 (the forced two-term balance).

## Scope / bug-guards

- No κ, no Λ, no G = κT. Exact over Q.
- bug-guard #4 (compress-then-normalize ρ_face): the pinned Gate-0 convention is used; it
  does not manufacture spurious criticality (no spurious linear term — δS_face = 0).
- If Gate 1 had FAILED (δS_face ≠ 0 anywhere, or I/3 not a max), the setup would be wrong
  and the run would abort. It PASSED ⇒ proceed to Gate 2.
