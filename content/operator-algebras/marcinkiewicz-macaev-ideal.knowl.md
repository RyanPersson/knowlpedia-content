+++
id = "operator-algebras/marcinkiewicz-macaev-ideal"
title = "Marcinkiewicz–Macaev ideal"
kind = "definition"
summary = "The compact-operator ideal defined by logarithmic bounds on partial sums of singular values."
aliases = ["Macaev ideal", "logarithmic Marcinkiewicz ideal", "M-1-infinity ideal"]
domains = ["operator-algebras", "noncommutative-geometry", "functional-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/hilbert-space", "functional-analysis/singular-values", "linear-algebra/compact-operator", "real-analysis/partial-sums"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(H\) be a separable [[linear-algebra/hilbert-space|Hilbert space]], and let
\(\mu_n(T)\) be the [[functional-analysis/singular-values|singular values]] of
a [[linear-algebra/compact-operator|compact operator]] \(T\), in nonincreasing
order. The **Marcinkiewicz–Macaev ideal** is
\[
\mathcal M_{1,\infty}(H)
=\left\{T:\sup_{N\geq 1}\frac{1}{\log(1+N)}
\sum_{n=1}^{N}\mu_n(T)<\infty\right\}.
\]
The displayed supremum defines an equivalent standard ideal norm. This logarithmic Marcinkiewicz ideal, often denoted \(\mathcal L^{(1,\infty)}\), is a two-sided symmetric operator ideal. Its condition controls Cesàro-type [[real-analysis/partial-sums|partial sums]] rather than each individual singular value.

## Comparison with the weak Schatten endpoint

The [[operator-algebras/weak-schatten-ideal|weak Schatten ideal]] at \(p=1\) is
\[
\mathcal L^{1,\infty}_{\mathrm{weak}}
=\{T:\sup_{n\geq1}n\mu_n(T)<\infty\}.
\]
It embeds continuously in \(\mathcal M_{1,\infty}\), since
\(\sum_{n\leq N}n^{-1}=O(\log N)\). The inclusion is strict: logarithmic control of an accumulated sum does not impose a uniform \(O(1/n)\) bound on every singular value. Consequently, notation such as \(\mathcal L^{1,\infty}\) is unsafe unless the author states whether it means weak-\(\ell^1\) decay or the larger logarithmic Marcinkiewicz ideal.

## Singular traces

For \(T\geq0\) in \(\mathcal M_{1,\infty}\), the logarithmic means
\[
\frac{1}{\log(1+N)}\sum_{n=1}^{N}\mu_n(T)
\]
form a [[real-analysis/bounded-sequence|bounded sequence]]. Applying a suitably invariant generalized limit gives a [[operator-algebras/dixmier-trace|Dixmier trace]]. This trace vanishes on trace-class operators and can detect the coefficient of critical logarithmic divergence. Membership in the ideal does not by itself make the value independent of the chosen generalized limit; that independence is an additional measurability property.

## Conventions and scope

The names “Macaev ideal,” “Dixmier ideal,” and “weak trace ideal” are not used uniformly. Some sources reserve the Macaev notation for a Köthe-dual ideal, while noncommutative-geometry sources commonly use \(\mathcal L^{(1,\infty)}\) for the logarithmic ideal defined here. This knowl fixes the partial-sum convention. More general Marcinkiewicz ideals replace \(\log(1+N)\) by another increasing concave control function.

## References

1. S. Lord, A. Sedaev, and F. Sukochev, “Dixmier Traces as Singular Symmetric Functionals and Applications to Measurable Operators,” *Journal of Functional Analysis* 224 (2005), 72–106. [DOI record](https://doi.org/10.1016/j.jfa.2005.01.002). Relevant: the logarithmic ideal \(\mathcal L^{(1,\infty)}\), Marcinkiewicz operator spaces, and measurable operators.
2. S. Lord, F. Sukochev, and D. Zanin, *Singular Traces: Theory and Applications*, De Gruyter, 2013. [Publisher record](https://doi.org/10.1515/9783110262551). Relevant: chapters 3 and 5 on symmetric operator ideals and Dixmier traces.
3. A. Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-maintained text](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf). Relevant: Chapter IV, §2 on infinitesimals of order one and the Dixmier trace.
