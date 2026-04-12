# Paper 8 Consistency Report

Checked files: main.tex, preamble.sty, refs.bib, and all 10 section files.

---

## 1. Label Resolution

### Defined labels (97 total)

All `\label{}` targets extracted across all files. All `\ref{}` and `\eqref{}` targets resolve to a defined label, with one exception noted below.

### Unresolved references: NONE

Every `\ref{...}` and `\eqref{...}` target has a corresponding `\label{...}`. No dangling references found.

### Duplicate label

- **`sec:gradient`** is defined as an alias on gradient-gapc.tex line 7 (`\label{sec:gradient}% alias for cross-refs from Sec.~2`), in addition to the primary label `sec:gradient-gapc` on line 6. This is intentional (used by entropy.tex line 13: `Sec.~\ref{sec:gradient}`), but note that LaTeX will silently use the second label's location for any `\ref{sec:gradient}` since both labels attach to the same sectioning command. **No action needed** -- this works correctly.

---

## 2. Citation Resolution

### Missing bibliography entries (BLOCKER)

Two citation keys appear in the text but have no entry in refs.bib:

| Key | Location | Context |
|-----|----------|---------|
| `Short2012` | appendix-assumptions.tex line 57 | "extending~\cite{Short2012} to SWAP lattices" |
| `Malament1977` | appendix-assumptions.tex line 75 | "via Malament's theorem~\cite{Malament1977}" |

These will produce **undefined citation warnings** and render as `[?]` in the compiled PDF.

### Uncited bibliography entries (minor)

Three bib entries are defined in refs.bib but never cited in any section file:

| Key | Entry |
|-----|-------|
| `Baez2002` | Baez, "The Octonions" |
| `PatiSalam1974` | Pati & Salam, "Lepton number as the fourth color" |
| `vandeWetering2019` | van de Wetering, "An effect-theoretic reconstruction of quantum theory" |

These compile without error but produce no output. They may be intentional (carried from Paper 7 for reference) or orphaned.

---

## 3. Notation Consistency

### 3a. Boltzmann constant: `\kB` vs raw `k_B`

`\kB` (rendering as `k_B`) is used consistently via the macro in all section files **except the abstract**:

- abstract.tex line 12: `$W \geq k_B T\, I(B;M)$` -- uses raw `k_B` and raw `I(B;M)` instead of `\kB` and `\MI{B}{M}`.

This is documented at the top of abstract.tex: `% NOTE: No macros used; abstract must be self-contained.` The rendered output is identical, so this is **intentional and correct**.

### 3b. Mutual information: `\MI{B}{M}` vs raw `I(B;M)`

Same situation as 3a. The abstract uses raw `I(B;M)` (line 12); all other files use `\MI{B}{M}` consistently. The `\MI` macro expands to `I(#1;#2)`, so rendered output matches. **No issue.**

### 3c. Experiential density: `\rhoexp` vs `\rho`

- The preamble defines `\newcommand{\rhoexp}{\rho}` (line 23), so `\rhoexp` renders identically to `\rho`.
- The abstract (line 23) uses raw `\rho = 0` instead of `\rhoexp = 0`.
- All section files consistently use `\rhoexp`.

**No rendered inconsistency**, since the macro maps to `\rho` anyway.

### 3d. Entropy in nats

Consistent throughout. The binary entropy (entropy.tex line 118) uses `\ln` (natural log), the von Neumann entropy is `S(\rho) = -\Tr(\rho \ln \rho)`, and all numerical entropy values are in nats. **No issue.**

### 3e. Clifford algebra conventions

- **Internal (Euclidean):** `Cl(6)` with `{gamma_i, gamma_j} = 2 delta_{ij}`, used in chirality-time.tex for the volume form omega_6. Consistent with Paper 7.
- **Spacetime (Lorentzian):** `Cl(d-1,1)` with mostly-minus metric `eta = diag(+1,-1,...,-1)`, so `Gamma_0^2 = +1`, `Gamma_i^2 = -1`. Used in chirality-time.tex.

The ASSERT_CONVENTION header on chirality-time.tex (line 2) says `clifford_convention=euclidean_positive_for_Cl6_lorentzian_mostly_minus_for_Cl(d-1,1)` and `metric=mostly_minus`, consistent with the text. **No issue.**

---

## 4. Convention / Numbering Consistency

### 4a. CRITICAL: Assumption numbering conflict between chirality-time.tex and the rest of the paper

The paper uses **two different numbering schemes** for assumptions labeled A1--A7, creating a conflict:

**Scheme 1 (chirality-time.tex, Theorem 3 assumptions, lines 269-281):**
| ID | Meaning |
|----|---------|
| A1 | h_3(O) is the universe algebra (Gap A) |
| A2 | Observer selects E_{11} (Gap B1) |
| A3 | Complex structure u in S^6 (Gap B2) |
| A4 | Complexification principle (Gap C) |
| A5 | Continuum limit yields smooth manifold |
| A6 | Lorentzian signature |

**Scheme 2 (gradient-gapc.tex Table 2, landauer.tex, predictions.tex, appendix-assumptions.tex):**
| ID | Meaning |
|----|---------|
| A1 | Finite-dimensional QM |
| A2 | Thermal contact at temperature T |
| A3 | Closed system equilibrates on finite timescales |
| A4 | SWAP lattice dynamics H = JF |
| A5 | Experiential density formula rhoexp |
| A6 | Continuum limit yields smooth manifold |
| A7 | Lorentzian signature |

The three-consequence theorem in chirality-time.tex uses A1-A6 to mean algebraic/geometric assumptions inherited from Paper 7, while the master theorem and all tables use A1-A7 to mean thermodynamic framework assumptions. **These are completely different numberings for different sets of assumptions sharing the same labels.**

Specific conflicts:
- **A1**: "h_3(O) is universe algebra" (Sec 4) vs "Finite-dimensional QM" (everywhere else)
- **A2**: "Observer selects E_{11}" (Sec 4) vs "Thermal contact" (everywhere else)
- **A3**: "Complex structure u" (Sec 4) vs "Closed system equilibrates" (everywhere else)
- **A4**: "Complexification principle" (Sec 4) vs "SWAP lattice dynamics" (everywhere else)
- **A5**: "Continuum limit" (Sec 4) vs "Experiential density formula" (Tables 1, prediction table, dep-map)
- **A6**: "Lorentzian signature" (Sec 4) vs "Continuum limit" (Tables elsewhere)

A reader encountering "A5" in the prediction table (meaning experiential density formula) and "A5" in Theorem 3 (meaning continuum limit) will be confused.

**Note:** The chirality-time.tex assumptions at lines 218-226 (Assumption A5, Assumption A6 as paragraph headers) use the scheme that MATCHES the main tables (A5 = continuum, A6 = Lorentzian), but the itemized list in the three-consequence theorem (lines 269-281) uses a completely different scheme. So even within chirality-time.tex there are two numbering systems.

### 4b. A9 naming conflict

- predictions.tex line 73: `A9 (Penrose initial entropy)` -- A9 is the Penrose initial entropy estimate ~10^88
- appendix-assumptions.tex line 121: `A9 & Neural self-modeling dimension d_M` -- A9 is the neural dimension

These describe **different parameters**. In predictions.tex, A9 = Penrose's S_initial ~ 10^88, and A10 = self-modeling parameters (d_M, nu). In the appendix table, A9 = neural dimension d_M, and A10 = update rate nu. The Penrose estimate moved into A8 territory (which covers S_max in the appendix but S_max AND S_initial overlap in the text).

Looking more carefully: predictions.tex has A8 = S_max ~ 10^122 (cosmological entropy budget), A9 = S_initial ~ 10^88 (Penrose initial entropy), A10 = self-modeling parameters (d_M ~ 10^11, nu ~ 10 Hz). The appendix has A8 = S_max ~ 10^122, A9 = neural d_M ~ 10^11, A10 = update rate nu ~ 10 Hz. So the appendix folded the Penrose initial entropy into A8 and split the self-modeling parameters across A9 and A10, while predictions.tex keeps Penrose as a separate A9. **These are inconsistent packagings of the same inputs.**

### 4c. Introduction chain (6 steps) vs selection chain (7 steps)

- Introduction line 66: "a chain of **six** implications"
- gradient-gapc.tex lines 18, 185: "**seven**-step selection chain" / "seven-step contrapositive chain"
- Introduction line 184: "The **seven-step** selection chain"

These are actually different chains. The six-step chain in the introduction (Sec 1.2) runs forward: self-modeling -> free energy -> non-equilibrium -> entropy gradient -> time-orientation -> chirality -> complexification. The seven-step chain in Sec 5.2 runs backward (contrapositive): no complexification -> no chirality -> no time-oriented chiral matter -> no entropy gradient -> no sustained non-equilibrium -> no free energy -> no self-modeling -> rho=0. These have different counts because the contrapositive chain includes the final step "rho = 0" as a separate item and also splits "non-equilibrium" from "free energy" into two steps. **This is internally consistent but could confuse readers.** The introduction correctly says "six implications" for its own chain and "seven-step selection chain" for the other one. No fix needed.

### 4d. Theorem/proposition numbering

The theorem environments share a counter (preamble.sty lines 75-82). The numbering is:
- Proposition 1 (prop:three-regimes, entropy.tex)
- Theorem 1 (thm:landauer, landauer.tex) -- **Wait**: this is wrong. Since theorem, lemma, proposition, corollary all share the `theorem` counter, Proposition 1 increments it to 1, then Theorem comes next as Theorem 2.

Actually, looking at the revtex4-2 behavior: these are `\newtheorem` without `[section]`, so they count sequentially across the paper. The actual numbering would be: Proposition 1 (three-regimes), Theorem 2 (landauer), Corollary 3 (exhaustion), Proposition 4 (chain), Proposition 5 (chirality-flip), Corollary 6 (projector-exchange), Theorem 7 (three-consequence), Remark 8, Remark 9, Theorem 10 (entropy-gradient), Theorem 11 (complexification), Remark 12, Theorem 13 (master), Corollary 14 (nexus).

References use `\ref{thm:landauer}` etc., which LaTeX resolves to the correct counter value. **All cross-references to theorem numbers use label-based \ref, so they automatically resolve correctly regardless of the counter values.** No issue.

### 4e. Landauer bound statement consistency

The Landauer bound W_min = k_B T I(B;M) appears in:
- landauer.tex eq. (eq:landauer): boxed, W_min = k_B T I(B;M)
- gradient-gapc.tex line 52: W_min = k_B T I(B;M) > 0
- gradient-gapc.tex line 237: W_min = k_B T I(B;M)
- introduction.tex line 73: k_B T I(B;M) of work per cycle
- introduction.tex line 118: at least k_B T I(B;M) of work
- abstract.tex line 12: W >= k_B T I(B;M) per cycle

All consistent. **No issue.**

---

## 5. Duplicate Content

### Near-duplicate: Experiential density formula

The formula `rhoexp = I(B;M)(1 - I(B;M)/S_vN(rho_B))` appears in three locations:
- landauer.tex eq. (eq:rho-def), line 123
- predictions.tex eq. (eq:rho-profile), line 172
- gradient-gapc.tex line 245 (inline)
- gradient-gapc.tex line 578 (Table 2, A5 column)
- appendix-assumptions.tex line 77 (Table 3)

This is a core definition that legitimately needs restating in each context. **Not a problem.**

### Near-duplicate: General channel formula

The general channel formula appears in:
- entropy.tex eq. (eq:channel-general), line 87-89
- appendix-derivations.tex eq. (eq:general-boxed), line 261-265

The appendix explicitly rederives it from scratch, which is its purpose. **Not a problem.**

### Near-duplicate: "Non-claims" sections

There are three "non-claims" / "explicit non-claims" sections:
- introduction.tex lines 132-150 ("Not proved")
- landauer.tex lines 330-348 ("Explicit non-claims")
- gradient-gapc.tex lines 595-628 ("Explicit non-claims")
- predictions.tex lines 300-333 ("Non-claims")

Each covers different non-claims appropriate to its section. Some overlap:
- "The Past Hypothesis is not derived" appears in introduction (line 138), gradient-gapc.tex (line 612), and predictions.tex (line 307, NC-1). This is intentional repetition for reader convenience and epistemic honesty.

**Acceptable duplication. No fix needed.**

---

## 6. Placeholder Detection

**No placeholders found.** Searched for TODO, FIXME, TBD, XXX, RESULT PENDING, PLACEHOLDER (case-insensitive) across all files. Clean.

---

## 7. Physics Consistency

### 7a. Entropy change formula

The single-step entropy change (entropy.tex eq. eq:entropy-change):
Delta S = h(lambda + p(1/2 - lambda)) - h(lambda) >= 0

Referenced correctly in gradient-gapc.tex via the monotonicity chain and convergence rate. **Consistent.**

### 7b. Channel formula E(rho_B)

The depolarizing channel (entropy.tex eq. eq:depolarizing):
E(rho_B) = (1-p) rho_B + p (1/2)

Used consistently in entropy.tex, appendix-derivations.tex, and referenced in gradient-gapc.tex. The general channel formula (eq:channel-general) correctly reduces to this when rho_M = 1/2 (explicitly verified in appendix-derivations.tex line 270-272). **Consistent.**

### 7c. Three-consequence theorem consistency

The theorem states u determines: (a) gauge group, (b) chirality, (c) time-orientation requirement.

- Introduction (line 120-124): "the single choice u in S^6 determines the gauge group, chirality, and the requirement for spacetime time-orientation---extending Paper 7's 'one choice, two consequences' to three." **Matches.**
- chirality-time.tex Theorem (thm:three-consequence): (a) Gauge group, (b) Chirality, (c) Time-orientation requirement. **Matches.**
- gradient-gapc.tex: References the theorem correctly via \ref throughout. **Matches.**
- discussion.tex (line 150): "Chirality <-> time-orientation (Theorem ref)." **Matches.**

**Consistent across all sections.**

### 7d. Quantitative numbers

| Quantity | Abstract | Predictions (Sec 6) | App. B | Consistent? |
|----------|----------|---------------------|--------|-------------|
| S_max | 10^122 | 10^122 (eq:smax-cosmo) | 10^122 | YES |
| S_initial | -- | 10^88 (eq:penrose-s) | -- | YES |
| Delta S_Landauer | ~10^28 | 3 x 10^28 (eq:delta-s-landauer) | -- | YES |
| Gap magnitude | 94 orders | 10^{-94} (eq:gap-94) | -- | YES |
| tau_exhaust | ~10^93 x t_U | 10^93 (eq:tau-ratio) | -- | YES |
| tau_exhaust (seconds) | -- | 10^111 s (eq:tau-value) | -- | YES |
| I(B;M) | -- | 7 x 10^9 nats | -- | YES |
| N_cycles | -- | 4 x 10^18 | -- | YES |

Cross-check: 10^122 / (7 x 10^9) x 0.1 = 10^122 / (7 x 10^10) ~ 1.4 x 10^111 ~ 10^111 s. Check.
10^111 / (4 x 10^17) ~ 2.5 x 10^93 ~ 10^93. Check.
3 x 10^28 / 10^122 = 3 x 10^{-94} ~ 10^{-94}. Check.

**All quantitative values are internally consistent.**

### 7e. Exhaustion timescale: abstract says 10^93 (ratio), predictions says 10^93 (ratio) and 10^111 s (absolute)

Abstract line 27: "the exhaustion timescale exceeds the age of the universe by ~10^93". Predictions eq. (eq:tau-ratio): tau_ex / t_U ~ 10^93. **Consistent.**

---

## Summary of Issues

### Blockers (will cause LaTeX compilation errors or visible [?] marks)

1. **Missing bib entries:** `Short2012` and `Malament1977` are cited but not defined in refs.bib.

### Significant (reader confusion, potential reviewer objection)

2. **Assumption numbering collision:** The three-consequence theorem (chirality-time.tex lines 269-281) uses A1-A6 with completely different meanings than the framework assumption table (gradient-gapc.tex Table 2, appendix-assumptions.tex). A reader seeing "A3" in Theorem 3 (meaning "complex structure u") and "A3" in Table 2 (meaning "closed system equilibrates") will be confused.

3. **A9 definition inconsistency:** predictions.tex defines A9 as "Penrose initial entropy ~10^88" while appendix-assumptions.tex defines A9 as "Neural self-modeling dimension d_M ~10^11". These are different parameters.

### Minor (cleanup, no physics impact)

4. **Uncited bib entries:** `Baez2002`, `PatiSalam1974`, `vandeWetering2019` are defined but never cited. Remove or cite.

5. **Route B assumption listing inconsistency:** The routes table (gradient-gapc.tex line 165) lists Route B assumptions as "A1, A3, A4". But Route B's text (lines 86-116) uses only finitude (A1), monotonicity (proven), and the fact that S_max implies maximally mixed state. A4 (SWAP lattice dynamics) does not appear to be required for Route B -- it enters only through the specific equilibration rate, which Route B does not use. The dep-map table (appendix-assumptions.tex line 172) correctly lists Route B as "A1, A3" without A4. **The routes comparison table is inconsistent with the dependency map.**

6. **P3 assumption listing:** predictions.tex line 281 says P3 ("rhoexp = 0 at equilibrium") depends on "A1, A5". Under the main numbering, A5 = experiential density formula. But in the chirality-time.tex scheme, A5 = continuum limit. Since the prediction table uses the main numbering, this is correct (P3 does depend on A1 and the rhoexp formula). However, the numbering collision from issue #2 makes this ambiguous to the reader.
