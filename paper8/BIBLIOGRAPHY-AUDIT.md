# Bibliography Audit Report -- paper8/refs.bib

**Audit date:** 2026-03-25
**Total entries:** 22
**Databases consulted:** INSPIRE-HEP, ADS, arXiv, Springer, APS, ScienceDirect

## Summary Statistics

| Status       | Count |
|--------------|-------|
| VERIFIED     | 14    |
| CORRECTED    | 3     |
| SELF-CITATION| 3     |
| FLAGGED      | 2     |

**Hallucinated references: 0**
All entries correspond to real papers.

---

## Corrections Needed

### 1. `Furey2018` -- WRONG arXiv eprint

The bib entry lists `eprint = {1806.00612}`, but arXiv:1806.00612 is a *different* Furey paper:
"SU(3)\_C x SU(2)\_L x U(1)\_Y (x U(1)\_X) as a symmetry of division algebraic ladder operators" (Eur. Phys. J. C 78, 375, 2018).

The paper "Three generations, two unbroken gauge symmetries, and one eight-dimensional algebra" (Phys. Lett. B 785, 84--89, 2018) has arXiv ID **1910.08395** (submitted Oct 2019, but journal publication is 2018).

**Fix:** Change `eprint = {1806.00612}` to `eprint = {1910.08395}`.

### 2. `TodorovDrenska2018` -- WRONG title

The bib entry title is "Composition algebras, exceptional Jordan algebra and related groups".
The actual title of arXiv:1805.06739 is **"Octonions, exceptional Jordan algebra and the role of the group F\_4 in particle physics"**.

"Composition algebras, exceptional Jordan algebra and related groups" is a *different* Todorov paper published in J. Geom. Symmetry Phys. 46, 59--93 (2017).

The entry also lacks the published journal reference. arXiv:1805.06739 was published in Adv. Appl. Clifford Algebras 28, 82 (2018), DOI: 10.1007/s00006-018-0899-y.

**Fix:** Correct the title to "Octonions, exceptional {Jordan} algebra and the role of the group $F_4$ in particle physics" and add the journal/DOI.

### 3. `Short2012` -- WRONG citation key year and volume/year inconsistency

The citation key says `Short2012` but the entry has `year = {2011}`. The paper was published in New J. Phys. 13, 053009 (2011), not 2012. The volume field also says `13` which matches 2011, not 2012.

Additionally the `pages` field says `053009` but the `volume` field says `13` -- both correct for 2011.

**Fix:** Either rename the key to `Short2011` (if nothing in the .tex files depends on the key `Short2012`), or at minimum note the year discrepancy. The metadata `year = {2011}` is correct; only the citation key is misleading.

---

## Flagged Entries

### 4. `Penrose1979` -- entry type mismatch

This is a chapter in an edited volume but is typed as `@article`. It uses both `journal`-style and `booktitle`/`editor`/`publisher` fields (which is unusual for `@article`). Should be `@incollection` or `@inbook`.

Not a correctness error in the metadata itself (all fields are accurate), but a BibTeX entry type issue.

### 5. `vandeWetering2019` -- missing journal reference

The paper was published in Compositionality, Volume 1 (2019), DOI: 10.32408/compositionality-1-1. The bib entry only has the arXiv preprint information. Adding the journal reference would strengthen the citation.

---

## Entry-by-Entry Verification

### Self-Citations

| Key    | Status       | Notes |
|--------|-------------|-------|
| Paper5 | SELF-CITATION | Unpublished manuscript in this series |
| Paper6 | SELF-CITATION | Unpublished manuscript in this series |
| Paper7 | SELF-CITATION | Unpublished manuscript in this series |

### External References

| Key | Status | Verification Source | Notes |
|-----|--------|-------------------|-------|
| Landauer1961 | VERIFIED | ACM, IEEE Xplore | IBM J. Res. Dev. 5, 183--191 (1961). DOI correct. |
| Bennett1982 | VERIFIED | Springer | Int. J. Theor. Phys. 21, 905--940 (1982). DOI correct. |
| ReebWolf2014 | VERIFIED | arXiv, IOP | New J. Phys. 16, 103011 (2014). arXiv:1306.4352. All metadata correct. |
| SagawaUeda2010 | VERIFIED | APS, arXiv | Phys. Rev. Lett. 104, 090602 (2010). arXiv:0907.4914. All metadata correct. |
| Lindblad1975 | VERIFIED | Springer, ADS | Commun. Math. Phys. 40, 147--151 (1975). DOI correct. |
| LawsonMichelsohn1989 | VERIFIED | Princeton Univ. Press | Spin Geometry, PUP (1989). ISBN 0-691-08542-0. Correct. |
| Penrose1979 | FLAGGED | ADS, academic refs | Metadata correct (pp. 581--638 in Hawking & Israel 1979). Entry type should be @incollection not @article. |
| Albert2000 | VERIFIED | Harvard Univ. Press | Time and Chance, HUP (2000). Correct. |
| Hoffman2015 | VERIFIED | Springer, PubMed | Psychon. Bull. Rev. 22, 1480--1506 (2015). DOI correct. |
| Furey2018 | CORRECTED | ScienceDirect, arXiv | Journal ref correct (Phys. Lett. B 785, 84--89, 2018). **arXiv eprint is wrong**: 1806.00612 is a different paper. Correct eprint: 1910.08395. |
| Boyle2020 | VERIFIED | arXiv | Preprint only (arXiv:2006.16265). Not published in a journal. Metadata correct for a preprint. |
| TodorovDrenska2018 | CORRECTED | arXiv, Springer | **Title is wrong.** Actual title of 1805.06739: "Octonions, exceptional Jordan algebra and the role of the group F\_4 in particle physics". Published in Adv. Appl. Clifford Algebras 28, 82 (2018). |
| BGW2020 | VERIFIED | Quantum journal, arXiv | Quantum 4, 359 (2020). arXiv:1606.09331. DOI correct. |
| CCM2007 | VERIFIED | arXiv, Int. Press | Adv. Theor. Math. Phys. 11, 991--1089 (2007). arXiv:hep-th/0610241. DOI correct. |
| Jacobson1995 | VERIFIED | APS, arXiv, INSPIRE | Phys. Rev. Lett. 75, 1260--1263 (1995). arXiv:gr-qc/9504004. DOI correct. |
| JvNW1934 | VERIFIED | JSTOR, academic refs | Ann. Math. 35, 29--64 (1934). DOI correct. |
| PatiSalam1974 | VERIFIED | APS, INSPIRE | Phys. Rev. D 10, 275--289 (1974). DOI correct. Note: there is an erratum (Phys. Rev. D 11, 703, 1975) but that is not required to cite. |
| Baez2002 | VERIFIED | AMS, arXiv | Bull. Amer. Math. Soc. 39, 145--205 (2002). arXiv:math/0105155. DOI correct. |
| vandeWetering2019 | FLAGGED | arXiv, Compositionality | Paper exists and is published in Compositionality 1 (2019), DOI: 10.32408/compositionality-1-1. Bib entry missing journal info. |
| Short2012 | CORRECTED | arXiv, IOP, ADS | New J. Phys. 13, 053009 (2011). arXiv:1012.4622. Key says "2012" but year is 2011. Metadata year is correct; key is misleading. |
| Malament1977 | VERIFIED | ADS, OSTI | J. Math. Phys. 18, 1399--1404 (1977). DOI correct. |
