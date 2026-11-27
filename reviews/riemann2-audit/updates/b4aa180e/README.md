# Review of changes through `b4aa180e`

The next review verifies the three author responses and covers the second half of unfolding. [Review through `9712a76c`](../9712a76c/README.md)

Two translation commits added 90 individual knowls and one chapter and revised four existing pages since `b92603a3`. This update compares all **95 changed pages** with the readable Lean source at `72fead10`. It records **95 new page findings on 56 pages**. The review assigns 12 high, 38 medium and 45 low priority. Each finding links the translation and the relevant Lean declaration and gives a proposed correction. [All findings as a table](findings.tsv) · [Translation diff](https://github.com/RyanPersson/knowlpedia-content/compare/b92603a3a52816e176d8237255fd9e572f9cbdbe...b4aa180eb8c6458b06da8af94de844de0e5e2d91) · [Report and tooling diff](https://github.com/RyanPersson/knowlpedia/compare/8e8b0ea628a689eaa11435adec77acaf51002668...d1e5326095b2b9484172c8129e0aed23b5456711)

| Area | New knowls | New chapters | Revised pages | Changed pages reviewed |
| --- | ---: | ---: | ---: | ---: |
| [Bessel continuation and spanning core](spanning-core.md) | 14 | 0 | 2 | 16 |
| [Unfolding of the Poincaré series](spanning-unfolding-a.md) | 76 | 1 | 2 | 79 |
| **Total** | **90** | **1** | **4** | **95** |

The 90 new individual knowls include 62 proofs marked `full`, 11 marked `outline` and 17 pages without a proof-status field. Each changed page and its presented argument was compared with the source. Each finding initially rated high priority received a second, independent source check. The earlier report covers the other 640 pages. During the review, `8835566d` merged that earlier report into `riemann2`. The content tree at the merge is identical to `b4aa180e`. [Previous audit](../../README.md) · [Findings on revised pages](coverage.md) · [Merge diff](https://github.com/RyanPersson/knowlpedia-content/compare/b4aa180eb8c6458b06da8af94de844de0e5e2d91...8835566df7e272d301d0a0b1d3782a50cdf3eb22)

## Findings that affect the mathematics

- **Uniform convergence is stronger than the proved estimate.** The sum of the absolute values is bounded by a constant independent of the adelic point. For a nonzero seed, evaluating a translate at the inverse translate of one fixed point gives the same nonzero value for every group element. The individual terms therefore cannot tend to zero uniformly on the whole group. [Convergence of the series](spanning-unfolding-a.md#page-convergence-of-poincare-series) · [Chapter wording](spanning-unfolding-a.md#page-spanning-unfolding-a)

- **Theorem B gives a dimension bound for the span.** The new introduction describes the translates as spanning the target. The source proves a lower bound of $(1-4/b^2)\dim T$ on their span. The same paragraph describes a second moment using squares of complex Petersson products where the source sums squared absolute values. [Chapter and sources](spanning-unfolding-a.md#page-spanning-unfolding-a)

- **The open-cell proof applies its Haar density twice.** With $d=\mathsf g(Z)/2$ and $c=c_Gd^{k-1}$, Lean multiplies product Haar measure by $c$ once. Substituting $c$ into the already-weighted fixer measure changes the mass and the resulting bound. [Normalization and correction](spanning-core.md#page-open-cell-bound-exists)

- **One-based frame labels collide with zero-based levels.** The formulas as printed place the final isotropic vector, the middle block and its dual at the same level, excluding valid unipotent elements. With labels $1\le a\le\varrho$, the isotropic and dual levels are $a-1$ and $2\varrho-a+1$. [Eichler elements](spanning-unfolding-a.md#page-eichler-elements-of-unipotent-congruence-subgroup) · [Row-additivity proof](spanning-unfolding-a.md#page-additivity-of-unipotent-row-entries)

## All high-priority findings

A mathematical issue repeated on two different pages has an entry for each place that needs an edit. The TSV also includes the medium- and low-priority findings. [Sortable table](findings.tsv)

- [Normalize the test function in the quantitative pairing bound](spanning-core.md#finding-spanning-core-1) · Spanning: the second moment, equal multiplicities, and Bessel systems
- [Use the global size parameter for the stationary-point entry bound](spanning-core.md#finding-bessel-systems-exist-at-the-real-places-1) · Bessel systems exist at the real places
- [The proof applies the fixer-measure density twice](spanning-core.md#finding-open-cell-bound-exists-1) · The open cell bound holds for every Bessel system
- [The second moment sums squared absolute values of Petersson products](spanning-unfolding-a.md#finding-spanning-unfolding-a-1) · Spanning: unfolding, part A (cutoffs, block sums, Poincaré series and the Bessel period)
- [Theorem B bounds the dimension of the span](spanning-unfolding-a.md#finding-spanning-unfolding-a-2) · Spanning: unfolding, part A (cutoffs, block sums, Poincaré series and the Bessel period)
- [Bound frame vectors on each Bessel-length layer](spanning-unfolding-a.md#finding-spanning-unfolding-a-3) · Spanning: unfolding, part A (cutoffs, block sums, Poincaré series and the Bessel period)
- [The Poincaré series have uniformly bounded absolute sums](spanning-unfolding-a.md#finding-spanning-unfolding-a-4) · Spanning: unfolding, part A (cutoffs, block sums, Poincaré series and the Bessel period)
- [Normalize the generic character before identifying the Bessel period](spanning-unfolding-a.md#finding-spanning-unfolding-a-5) · Spanning: unfolding, part A (cutoffs, block sums, Poincaré series and the Bessel period)
- [The displayed levels identify the last hyperbolic pair with the middle block](spanning-unfolding-a.md#finding-additivity-of-unipotent-row-entries-1) · Additivity of a row entry under right multiplication in the unipotent group
- [A uniform bound for the absolute sums does not give uniform convergence on G](spanning-unfolding-a.md#finding-convergence-of-poincare-series-1) · Uniform convergence of the Poincaré series and integrability of the cut-off Bessel functions
- [Separate the last isotropic, middle and first dual levels](spanning-unfolding-a.md#finding-eichler-elements-of-unipotent-congruence-subgroup-1) · Eichler elements of the unipotent congruence subgroups
- [Group the summands with the unipotent factor on the left](spanning-unfolding-a.md#finding-poincare-series-are-forms-1) · The Poincaré series are forms of the discrete series type and principal level

## Questions the translators raised

The seven outstanding Bessel files now have translations. The 11 files in unfolding A total 8,177 source lines. The area has 352 distinct front-matter declaration names, and its source-file assignment is disjoint from the eight files reserved for unfolding B. The 12 existing B drafts all cite `Setup.lean`. The new chapter links all 81 of its individual pages. [Coverage and report corrections](coverage.md)

The review traced 72 library declarations or uses called out by the authors and related claims to their precise statements. The period exponent and phase, the Schur degree factors, the Petersson convention and its volume ratio agree with the source. Among the corrections are the global parameter $3D.a$ in the stationary-point proof and the field-degree assumption in the local-bounds application. [Library comparisons](library-checks.md) · [Existence at the real places](spanning-core.md#page-bessel-systems-exist-at-the-real-places)

The Sobolev quotation now includes $0<\varepsilon\le1$ and uses ordinary integrals. This resolves one of the six earlier findings on the four amended pages. The other five remain open. [Exact disposition](coverage.md)

## Build and references

The production compiler generated all 735 Riemann2 pages and reported the same ten existing missing links. Two now have published target pages. All 5,393 math expressions on the changed pages parsed. The review also checks 473 front-matter names, 251 distinct Lean placeholder names, all 73 newly added concept proposals, and the new synchronization script. The concept review records 37 corrections to definitions or targets. [Build and publishing helper](build-and-tools.md) · [Lean reference checks](lean-references.md) · [Concept corrections](concepts.md)

These comparisons show later additions to either branch. [Subsequent translation changes](https://github.com/RyanPersson/knowlpedia-content/compare/8835566df7e272d301d0a0b1d3782a50cdf3eb22...riemann2) · [Subsequent report or tooling changes](https://github.com/RyanPersson/knowlpedia/compare/d1e5326095b2b9484172c8129e0aed23b5456711...riemann2)
