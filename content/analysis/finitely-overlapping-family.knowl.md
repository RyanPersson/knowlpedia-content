+++
id = "analysis/finitely-overlapping-family"
title = "Finitely overlapping family of sets"
kind = "definition"
summary = "A family of sets whose multiplicity function is uniformly bounded."
aliases = ["bounded overlap family", "uniformly finite overlap"]
domains = ["analysis", "measure-theory"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A family of sets \({E_j}_{j\in J}\) is **finitely overlapping with multiplicity
at most \(N\)** if
\[
\sum_{j\in J}\mathbf 1_{E_j}(x)\le N
\]
for every \(x\), or for almost every \(x\) when the statement is
measure-theoretic. The bound \(N\) is required to be independent of the size
and location of the family members.

## Integral consequence

For nonnegative measurable \(g\), [[measure-theory/tonellis-theorem|Tonelli's theorem]] gives
\[
\sum_j\int_{E_j}g\le N\int_{\bigcup_jE_j}g.
\]
Thus local estimates may be summed without accumulating a factor equal to the
number of sets.

## Typical construction

Euclidean annuli can be covered by equal-width cubes so that suitably enlarged
cubes have bounded overlap, with a multiplicity depending only on dimension.
This is the form used to assemble smooth weights from
[[differential-geometry/bump-function|bump functions]].

## References

1. Elias M. Stein, *Singular Integrals and Differentiability Properties of Functions*, Princeton University Press, 1970. [Publisher record](https://press.princeton.edu/books/paperback/9780691080796/singular-integrals-and-differentiability-properties-of-functions).
