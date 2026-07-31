+++
id = "noncommutative-geometry/metric-dimension"
title = "Metric dimension of a spectral triple"
kind = "definition"
summary = "The critical exponent at which powers of a spectral triple's regularized inverse Dirac operator become trace class."
aliases = ["spectral dimension", "summability dimension"]
domains = ["noncommutative-geometry", "functional-analysis"]
section_mode = "progressive"
+++

For a [[noncommutative-geometry/spectral-triple|spectral triple]] \((\mathcal A,H,D)\), its **metric dimension** is the critical summability exponent
\[
\dim_{\mathrm{met}}(D)=
\inf\left\{p>0:
\operatorname{Tr}\!\left((1+D^2)^{-p/2}\right)<\infty
\right\},
\]
with value \(+\infty\) if the set is empty. Equivalently, it is the infimum
of exponents for which the regularized inverse \((1+D^2)^{-1/2}\) belongs to
the corresponding [[functional-analysis/schatten-class-operator|Schatten ideal]].
The infimum need not be attained and need not be an integer. It depends on
the spectral growth of \(D\), including eigenvalue multiplicities, rather
than on the algebra alone.

## Counting-function interpretation

Let \(N_D(\Lambda)\) count eigenvalues of \(|D|\) not exceeding \(\Lambda\),
with multiplicity. Polynomial growth \(N_D(\Lambda)=O(\Lambda^d)\) implies
summability for every \(p>d\). Under a matching two-sided Weyl asymptotic
\(N_D(\Lambda)\sim C\Lambda^d\), the critical exponent equals \(d\), and
\((1+D^2)^{-1/2}\) has singular values of order \(n^{-1/d}\). It then lies at
the endpoint in the [[operator-algebras/weak-schatten-ideal|weak Schatten ideal]]
\(\mathcal L^{d,\infty}\), although generally not in \(\mathcal L^d\).

Without regular variation or comparable estimates, a critical exponent alone
does not imply weak-ideal membership at the endpoint.

## Canonical manifold case

For the canonical spin spectral triple of a closed \(d\)-dimensional
Riemannian spin manifold, Weyl's law gives metric dimension \(d\). The triple
is strictly \(p\)-summable for every \(p>d\), while \(|\not D|^{-d}\), with
the kernel removed, is of weak trace class. This analytic dimension agrees
with manifold dimension and supports the noncommutative integral
[Connes, Chapter VI, §1].

Rescaling \(D\) by a nonzero constant changes metric lengths but not the
critical exponent. Taking direct sums can change the dimension to the larger
of the component dimensions when both have polynomial spectral growth.

## Distinction from dimension spectrum

**Warning.** Metric dimension is one extended real number. The
[[noncommutative-geometry/dimension-spectrum|dimension spectrum]] is a set of
poles of an entire family of weighted spectral zeta functions and requires
regularity and meromorphic continuation. Its largest pole often equals the
metric dimension in geometric examples, but neither notion determines the
other in full generality.

Some authors reserve “spectral dimension” for a heat-kernel scaling exponent
or for the abscissa of convergence of \(\operatorname{Tr}(|D|^{-s})\). These
agree with the core under standard compact-resolvent conventions, after
removing the kernel, but borderline and infinite-dimensional cases require
care.

## References

1. A. Connes, *Noncommutative Geometry*, Academic Press, 1994. [Author-hosted text](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf). Relevant: Chapters IV and VI on infinitesimal order, summability, and the dimension of a canonical manifold triple.
2. J. M. Gracia-Bondía, J. C. Várilly, and H. Figueroa, *Elements of Noncommutative Geometry*, Birkhäuser, 2001. [DOI record](https://doi.org/10.1007/978-1-4612-0005-5). Relevant: §§10.1 and 10.5 on summability, spectral dimension, and zeta functions.
