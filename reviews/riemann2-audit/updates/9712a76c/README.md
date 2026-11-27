# Verification of the authors’ fixes and the second unfolding chapter

**All 61 original findings in the three author responses are resolved** at `9712a76c`, including the six originally rated high priority. The published `derivatives-vacuum` chapter, its 95 individual knowls, its concept table and its report match the previous snapshot. The coordinator names that chapter next, with 41 review findings awaiting a published response. [Finding-by-finding verification](response-ledger.tsv) · [Coordinator handoff](https://github.com/RyanPersson/knowlpedia/blob/12cc7330341b6b4fb72c78b91a659e67e82a4b18/docs/riemann2/STATE.md#L72) · [Vacuum findings](../../areas/derivatives-vacuum.md)

Four translation commits followed `8835566d`. They added 77 individual unfolding-B knowls and its chapter, edited 72 pages and retired one field-setting page. The review compared all 151 affected paths with the pinned Lean source at `72fead10` and also checked the four previously published, unedited pages in unfolding B. [Translation diff](https://github.com/RyanPersson/knowlpedia-content/compare/8835566df7e272d301d0a0b1d3782a50cdf3eb22...9712a76c5437e43a3c0af1665f02b9d9203c5bd8) · [Author reports and concept changes](https://github.com/RyanPersson/knowlpedia/compare/d1e5326095b2b9484172c8129e0aed23b5456711...12cc7330341b6b4fb72c78b91a659e67e82a4b18)

## Results by area

| Area | Prior findings checked | Resolved | Partly addressed | Open | Newly identified findings |
| --- | ---: | ---: | ---: | ---: | ---: |
| [derivatives-divisibility](derivatives-divisibility.md) | 20 | 20 | 0 | 0 | 8 |
| [reduction-main](reduction-main.md) | 22 | 22 | 0 | 0 | 2 |
| [reduction-zeros](reduction-zeros.md) | 19 | 19 | 0 | 0 | 0 |
| [spanning-unfolding-b](spanning-unfolding-b.md) | 7 | 0 | 3 | 4 | 53 |

The review identified **63 additional page-level findings on 45 pages** (2 high, 24 medium and 37 low). A newly identified issue may be on an unchanged sentence of a revised page. The full table includes the proposed edit and source line. Every new high finding and every previous high finding in this review received a second source check. [New findings](findings.tsv) · [Previous findings and dispositions](response-ledger.tsv)

## The divisibility response

The theta-product count now requires its multiplier $H$ to have integral coefficients in the indicated $y$-series. The exponential-scale norm bound is present in the chapter’s integrality criterion. The CM setting uses the normalized sigma function with the correct transformation law and distinguishes it from the classical Weierstrass sigma. The 20 resolved findings break down into three high, nine medium (on eight pages) and eight low. The area has 38 individual knowls, including 26 full proofs and one outline. [Integral multiplier](derivatives-divisibility.md#page-the-count) · [Scale bound](derivatives-divisibility.md#page-derivatives-divisibility) · [Sigma normalization](derivatives-divisibility.md#page-cm-curve-setting)

The revised Schur remark correctly reverses the old expansion, but it drops the rank and diagram compatibility assumed by Lean. With source rank two, target rank one, a single height-one column and $y=0$, the output is an empty minor product equal to one and all proposed source coefficients vanish. Add the `FitsRanks` hypotheses to the remark, and update the chapter’s summary of the expansion. [Counterexample and source](derivatives-divisibility.md#page-product-of-minors) · [Chapter wording](derivatives-divisibility.md#page-derivatives-divisibility)

The power-series cleanup removed all **54 literal bracket pairs across 16 files**, plus two plain-text summary spellings. A separate, pre-existing link inside display math still renders as literal text in `field-e-and-its-places`. All 12 pages that referred to the retired field-setting knowl now use the owner in `reduction-main`. The two retained setting pages refer to library declarations with no exact knowl owner. [Bracket counts, rendered output and field ownership](brackets.md)

## The second half of unfolding

All 89 individual knowls and the new chapter were compared with Lean. Its 61 full proofs and one outline reference eight assigned Lean files. The seven findings recorded on the old drafts still need work. Three have better citations or links but retain a missing qualification, and four remain open. One of those four still asserts a change of lattice basis over every ring, which fails in characteristic $N$. [Basis-change counterexample](spanning-unfolding-b.md#page-filling-data) · [All seven prior findings](response-ledger.tsv)

- **The whole-group moment bound needs positive type and an identity bound.** State the conditional bound with its two assumptions and Weil data. When the operator realization is introduced, explain how it supplies them. [Chapter and Lean source](spanning-unfolding-b.md#new-spanning-unfolding-b-1)
- **An amplitude-block realization must be unitary for equivariance and the total bound.** Introduce a finite-dimensional unitary ρ with respect to the inner product used for P\*, assume admissibility and the requisite field data, and distinguish the block identities that hold before unitarity is imposed. [Chapter and Lean source](spanning-unfolding-b.md#new-spanning-unfolding-b-2)

The determinant-sieve stabilizers, the normalization by the square of the unipotent covolume, the $b^{-12}$ estimate near the Bessel subgroup and the final $5b^{-4}$ near-isometry error agree with the source. The induced-character outline needs a lower bound for the volume of a local integral group to derive the constant two. [Library checks](library.md) · [Induced-character outline](spanning-unfolding-b.md#page-square-sum-of-the-induced-character)

## Published handoff and build

The new author prompt points to the original 353-finding audit. The 95 later findings on `spanning-core` and `spanning-unfolding-a` are on `riemann2-review`, and their pages have the same text at this snapshot. The response queue should include those findings as well as the unfolding-B review. [Published queue and report corrections](handoff.md) · [Previous incremental findings](../b4aa180e/findings.tsv)

The production compiler generated all **812 pages** with eight older missing-link errors, down from ten. All 43,823 math occurrences parsed. All 446 explicitly named declarations in the eight unfolding-B source files have a unique owner. A newly added Frobenius citation is missing its `QuadField` namespace. The concept review also identifies incorrect target assignments and statements needing tighter hypotheses. [Build](build.md) · [Lean names](provenance.md) · [Concept review](concepts.md)

[Changes after this content snapshot](https://github.com/RyanPersson/knowlpedia-content/compare/9712a76c5437e43a3c0af1665f02b9d9203c5bd8...riemann2) · [Subsequent author reports](https://github.com/RyanPersson/knowlpedia/compare/12cc7330341b6b4fb72c78b91a659e67e82a4b18...riemann2)
