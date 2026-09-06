+++
id = "operator-algebras/weak-schatten-ideal"
title = "Weak Schatten ideal"
kind = "definition"
summary = "The operator ideal of compact operators whose singular values decay at the weak-lp rate."
aliases = ["Lorentz operator ideal", "L-p-infinity", "weak trace ideal"]
domains = ["operator-algebras", "functional-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/hilbert-space", "linear-algebra/compact-operator", "functional-analysis/schatten-class-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(H\) be a [[linear-algebra/hilbert-space|Hilbert space]], let \(p>0\), and write \(\mu_n(T)\) for the singular values of a [[linear-algebra/compact-operator|compact operator]] \(T\), arranged in nonincreasing order and counted with multiplicity. The **weak Schatten ideal**
\[
\mathcal L^{p,\infty}(H)=\left\{T:\sup_{n\geq1}n^{1/p}\mu_n(T)<\infty\right\}
\]
consists exactly of compact operators satisfying \(\mu_n(T)=O(n^{-1/p})\). The displayed supremum is a natural quasinorm. This is a two-sided operator ideal, also called the weak-\(p\) or Lorentz operator ideal, and it is larger than the [[functional-analysis/schatten-class-operator|Schatten class]] \(\mathcal L^p(H)\).

## Comparison with Schatten classes

For \(0<q<p\), one has
\[
\mathcal L^q\subset\mathcal L^{p,\infty},
\]
and \(\mathcal L^p\subset\mathcal L^{p,\infty}\). The diagonal operator on \(\ell^2(\mathbb N)\) with eigenvalues \(n^{-1/p}\) lies in \(\mathcal L^{p,\infty}\) but not in \(\mathcal L^p\). Thus weak Schatten membership records a critical polynomial decay rate without requiring summability at the endpoint.

## Role in noncommutative geometry

Weak ideals express borderline spectral dimension: an inverse or resolvent whose singular values behave like \(n^{-1/p}\) is weakly \(p\)-summable. At \(p=1\), suitable positive operators can support singular traces, including Dixmier-type constructions. Membership alone does not ensure that every generalized limit produces the same trace value; that stronger property is measurability in the sense of singular traces.

## Conventions and scope

**Warning.** Notation is not uniform. “Weak trace ideal” normally refers only to the case \(p=1\). Some noncommutative-geometry sources use \(\mathcal L^{(1,\infty)}\) for the larger Marcinkiewicz ideal defined by logarithmic bounds on [[real-analysis/partial-sums|partial sums]] of singular values. That ideal must not be silently identified with the weak-\(\ell^1\) condition \(\sup_n n\mu_n(T)<\infty\) used here.

## References

1. S. Lord, F. Sukochev, and D. Zanin, *Singular Traces: Theory and Applications*, De Gruyter, 2013. [Publisher record](https://doi.org/10.1515/9783110262551). Relevant: symmetric operator ideals, weak ideals, and singular traces.
2. A. Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-maintained text](https://www.alainconnes.org/docs/book94bigpdf.pdf). Relevant: chapter IV, infinitesimals and Dixmier traces.
