---
domain: mathematical
category: convention-pitfall
severity: medium
confidence: single_observation
first_seen: 2026-05-26
last_seen: 2026-05-26
occurrence_count: 1
---

## Pattern: Exact-over-Q rank lock with module-local source guard

**What goes wrong:** Decisive invariant-theory ranks must use exact DomainMatrix-over-QQ, never numpy float-rank; a module-local source guard scanning __file__ for forbidden float-rank/float-engine imports catches convention drift and planted violations across phases

**Why it happens:** [Root cause to be documented]

**How to detect:** Grep the decisive harness for np.linalg.matrix_rank and float-engine imports; confirm a source-scan guard asserts 0 of each; re-run and check the guard fires on a planted violation

**How to prevent:** [Prevention guidance to be documented]

**Example:** [Example to be added]

**Test value:** [Numerical test to be added]
