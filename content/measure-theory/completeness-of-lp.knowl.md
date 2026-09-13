+++
id = "measure-theory/completeness-of-lp"
title = "Completeness of Lebesgue spaces"
kind = "theorem"
summary = "Every Cauchy sequence in Lp converges in Lp for 1 <= p <= infinity."
aliases = ["Riesz-Fischer completeness theorem", "Lp completeness"]
domains = ["measure-theory"]
section_mode = "progressive"
prerequisites = ["measure-theory/lp-space", "measure-theory/minkowski-inequality-lp", "measure-theory/monotone-convergence-theorem", "linear-algebra/banach-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For any measure space and \(1\le p\le\infty\), the space \(L^p\) is a [[linear-algebra/banach-space|Banach space]]: every sequence Cauchy in its norm has a limit in that norm.

## Summable-increment argument

From a Cauchy sequence choose a subsequence \(f_{n_j}\) with \(\|f_{n_{j+1}}-f_{n_j}\|_p\le2^{-j}\). For \(p<\infty\), Minkowski and monotone convergence imply that \(\sum_j|f_{n_{j+1}}-f_{n_j}|\) lies in \(L^p\), hence is finite almost everywhere. The telescoping series defines a limit, and its norm tail is at most \(\sum_{j\ge m}2^{-j}\). The Cauchy property brings the whole sequence to the same limit. For \(p=\infty\), remove the countable union of exceptional null sets; the increment series then converges uniformly there.

## References

- [John K. Hunter, Measure Theory, Chapters 4, 5 and 7](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes.pdf).
