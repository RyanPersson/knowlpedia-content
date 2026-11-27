# Audit of the Riemann2 translation

The latest review verifies 61 author fixes and the second half of unfolding through `9712a76c`. The preceding update covers the Bessel continuation and the first 11 unfolding files. [Author responses and unfolding B](updates/9712a76c/README.md) · [Earlier incremental review](updates/b4aa180e/README.md)

All **644 pages** added on `riemann2` through `b92603a3` were compared with the readable Lean edition. The scope includes 635 individual knowls and nine chapter pages in 17 areas. There are **353 page-level findings on 279 pages**. The review assigns 29 high, 172 medium, and 152 low priority. A recurring issue counts once on each affected page. Compiler diagnostics and the cross-area declaration-name checks are listed separately. [Findings with proposed edits](findings.tsv) · [Compiler and link results](structural-checks.md)

The review used the complete bodies, front matter, and available author reports. For each page, the area ledger identifies the source declaration, what was checked, and any correction. The comparison covered stated hypotheses, quantifiers, constants, normalization, and the steps presented in the human-readable proof. Outlines were checked at the depth they present, with additional source work on the questions the authors flagged. This is a translation audit. Lean was read as source, and its build and proof kernel were outside this review. [Content snapshot](https://github.com/RyanPersson/knowlpedia-content/tree/b92603a3a52816e176d8237255fd9e572f9cbdbe/content/proofs/grh) · [Author reports](https://github.com/RyanPersson/knowlpedia/tree/8e8b0ea628a689eaa11435adec77acaf51002668/docs/riemann2/reports) · [Lean source snapshot](https://github.com/lsernau/grh-lean/tree/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src)

## Findings to read first

- **The theta-product count needs an integral multiplier.** The application allows a factor $H$ without stating the integral-series condition in the cited theorem. For the empty diagram the jet is the constant coefficient. Taking $H=p^{-M}$ makes its norm $p^M$, which can exceed the claimed bound. [Knowl and source](areas/derivatives-divisibility.md#page-the-count)
- **The edge representatives and the Hecke cosets are on different sides in the translation.** At $g=1$, the matrices $\beta d$ parametrize cosets $\beta dK$. Writing $K\beta d$ makes every representative give the single coset $Kd$. This changes the sum over edges. [Coset comparison](areas/upper-divisibility.md#page-hecke-cosets-as-edges)
- **The invariant-average remark fails over the rings it permits.** With two singleton blocks over $\mathbb F_2$, the block diagonal group is trivial. Extracting the coefficient of $X_{01}$ is invariant and gives $1$ on a monomial with unequal row and column weights. The vanishing lemma imposes extra conditions on the coefficient rings. [Counterexample and hypotheses](areas/upper-elementary-divisors.md#page-conjugation-invariant-average)
- **The elementary-divisor chapter drops one unit from a root weight.** At the distinguished letter the coefficient of the positive root variable is $q/(q-1)$. The chapter gives $1/(q-1)$, so its defect calculation misses that variable’s exponent in every monomial that contains it. [Chapter formula and source](areas/upper-elementary-divisors.md#page-upper-elementary-divisors)
- **The split Hecke operator needs a value above the rank.** The eigensystem uses every $i\ge0$. For $i>r$ the displayed rank-$r$ diagonal representative cannot exist. In Lean the double coset is empty and the operator is zero. [Hecke operator definition](areas/spanning-core.md#page-hecke-operators-at-split-places)
- **The Gaussian theta sum requires a convergence convention.** At $j=0$, $u=1$, and $c(n)=\exp(\pi n^2)$, every summand in the displayed definition equals one. The unqualified tail integrals have a related convergence problem. [Theta sum](areas/reduction-zeros.md#page-theta-series-of-coefficients) · [Tail integrals](areas/reduction-zeros.md#page-theta-tail-integral-and-mollifier)

## Questions resolved from the translating agents’ reports

- **The eight repaired files.** All eight bodies, their headers, and their Lean references were reread. The committed repair removes eight duplicate reference blocks. Three summary corrections and a mistaken source citation survive in this group. The 67 elementary-divisor knowls and their index have identical Git objects across the repair. The same handoff review traces all ten library lemmas named by the authors, plus related measure and Sobolev lemmas, to their applications. [Collision evidence and 21 library comparisons](spanning-core-handoff.md)
- **The large-degree numerical outline.** All six consequences were checked against the intervening inequalities. In particular, $q\ge2^{40}$ gives $\log q\ge27$, the constant used in the exponent estimates. [Six quantitative checks](areas/upper-elementary-divisors.md#page-consequences-of-large-degree)
- **The final theorem statements and the real-variable estimate.** The five top-level translated statements preserve the scope of the pinned declarations, including the exception at the principal character’s pole. The one-sided estimate passes from integers to all large real arguments, with error $26/y$ and the constant $2C+26$ absorbed into $y^\delta$. [Five statements](areas/reduction-zeros.md#page-main-theorems) · [Real-argument estimate](areas/reduction-main.md#page-one-sided-bound)
- **The double-lift equivariance scalar.** The two zero-term stages cancel the apparent extra determinant character. The review records the three exponents before and after the rank change. [Determinant exponents](areas/upper-seesaw.md#page-double-lift-evaluation-equivariant)

## Coverage by area

The authors label 322 individual knowls `full` and 112 `outline`. The other 201 have no proof-status field. Of the pages labelled `full`, 109 have a review comment. Comments include local issues in definitions, summaries, proof arguments, or citations. The seven unread Bessel files have no standalone translations in this snapshot. [Spanning-core coverage](https://github.com/RyanPersson/knowlpedia/blob/8e8b0ea628a689eaa11435adec77acaf51002668/docs/riemann2/reports/spanning-core.md#L14)

| Area review | Translator status | Knowls | Full | Outline | Pages with comments¹ | High findings |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| [reduction-zeros](areas/reduction-zeros.md) | Finished | 59 | 47 | 2 | 18 | 2 |
| [reduction-main](areas/reduction-main.md) | Finished | 51 | 23 | 5 | 18 | 1 |
| [derivatives-divisibility](areas/derivatives-divisibility.md) | Finished | 39 | 26 | 1 | 16 | 3 |
| [derivatives-vacuum](areas/derivatives-vacuum.md) | Finished | 95 | 51 | 22 | 34 | 1 |
| [upper-objects](areas/upper-objects.md) | Finished | 64 | 16 | 14 | 31 | 6 |
| [upper-seesaw](areas/upper-seesaw.md) | Finished | 51 | 35 | 7 | 30 | 5 |
| [upper-divisibility](areas/upper-divisibility.md) | Finished | 60 | 7 | 42 | 33 | 2 |
| [upper-elementary-divisors](areas/upper-elementary-divisors.md) | Finished | 67 | 44 | 1 | 24 | 2 |
| [spanning-core](areas/spanning-core.md) | 10 of 17 Lean files | 52 | 22 | 11 | 32 | 4 |
| [spanning-unfolding-a](areas/spanning-unfolding-a.md) | Interrupted draft | 5 | 3 | 0 | 3 | 0 |
| [spanning-unfolding-b](areas/spanning-unfolding-b.md) | Interrupted draft | 12 | 2 | 0 | 7 | 1 |
| [spanning-mainterm](areas/spanning-mainterm.md) | Interrupted draft | 15 | 10 | 0 | 4 | 0 |
| [spanning-frames-b](areas/spanning-frames-b.md) | Interrupted draft | 15 | 7 | 0 | 5 | 1 |
| [determinant-exchange](areas/determinant-exchange.md) | Interrupted draft | 11 | 6 | 2 | 4 | 0 |
| [determinant-chain](areas/determinant-chain.md) | Interrupted draft | 14 | 10 | 0 | 5 | 0 |
| [onelift-comparison](areas/onelift-comparison.md) | Interrupted draft | 14 | 5 | 5 | 10 | 1 |
| [onelift-values](areas/onelift-values.md) | Interrupted draft | 11 | 8 | 0 | 5 | 0 |
| **Total** | | **635** | **322** | **112** | **279** | **29** |

¹ The two findings columns include the chapter page when one exists. The 97 knowls in the eight interrupted draft areas are included even though those areas have no published chapter pages.

## Priority and reproduction

High priority identifies errors that materially change a stated object, claim, or inference. Medium priority identifies a missing qualification or proof step, including incorrect applications or remarks where the main result survives. Low priority covers local attribution, notation, and smaller clarifications. Each finding initially rated high priority received an independent second source check. The tab-separated file contains the knowl ID, line, cited declaration, reasoning, and proposed correction for every page-level finding. [Findings table](findings.tsv) · [All high-priority findings](high-priority.md)

The production compiler generated all 644 selected HTML pages and returned ten missing-target errors on eight draft pages. All 35,270 math occurrences parsed with the project’s KaTeX version. The structural audit also records 35 incorrectly qualified Lean placeholder names and the assumptions needed to resolve the remaining ambiguous references. [Build and link evidence](structural-checks.md) · [Declaration-name audit](lean-references.md)

The initial seven-area review remains available at its original scope. The following comparisons pick up future commits independently in the content and author-report repositories. [First review](../riemann2-review.md) · [Content changes after this audit](https://github.com/RyanPersson/knowlpedia-content/compare/b92603a3a52816e176d8237255fd9e572f9cbdbe...riemann2) · [Report changes after this audit](https://github.com/RyanPersson/knowlpedia/compare/8e8b0ea628a689eaa11435adec77acaf51002668...riemann2)
