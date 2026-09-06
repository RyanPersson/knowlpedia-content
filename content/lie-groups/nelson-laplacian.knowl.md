+++
id = "lie-groups/nelson-laplacian"
title = "Nelson Laplacian"
kind = "definition"
summary = "The positive sum of squares of infinitesimal generators used to detect regular vectors in a unitary Lie-group representation."
aliases = ["representation Laplacian", "Nelson operator"]
domains = ["lie-groups", "harmonic-analysis", "functional-analysis"]
prerequisites = ["lie-groups/strongly-continuous-unitary-representation", "fiber-bundles/lie-group", "lie-groups/lie-algebra", "lie-groups/smooth-vector-unitary-representation", "functional-analysis/symmetric-operator"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\pi\) be a
[[lie-groups/strongly-continuous-unitary-representation|strongly continuous
unitary representation]] of a finite-dimensional
[[fiber-bundles/lie-group|Lie group]] \(G\) on \(H\), and choose a basis
\(X_1,\ldots,X_n\) of its real [[lie-groups/lie-algebra|Lie algebra]]. On the
common invariant domain \(H^\infty\) of
[[lie-groups/smooth-vector-unitary-representation|smooth vectors]], put
\[
\Delta_{\pi}=-\sum_{j=1}^{n}d\pi(X_j)^2.
\]
This nonnegative [[functional-analysis/symmetric-operator|symmetric
operator]] is the **Nelson Laplacian** of the representation. Some authors
instead call \(1+\Delta_\pi\) the Nelson
operator, or use the opposite sign for the Laplacian. The sign convention
above makes \(\Delta_\pi\) positive because each infinitesimal generator
\(d\pi(X_j)\) is skew-symmetric on \(H^\infty\).

## Closure and smooth vectors

The operator \(\Delta_\pi\) on \(H^\infty\) is
[[functional-analysis/essentially-self-adjoint-operator|essentially
self-adjoint]]. If
\(\overline{\Delta_\pi}\) denotes its nonnegative self-adjoint closure, then
\[
H^\infty=\bigcap_{k\geq 1}
\operatorname{Dom}\!\left(\overline{\Delta_\pi}^{\,k}\right).
\]
Thus powers of one elliptic operator encode simultaneous differentiability
under every derived operator. More generally, the topology on \(H^\infty\)
defined by the [[lie-groups/derived-representation-on-smooth-vectors|derived
action]] of the [[lie-groups/universal-enveloping-algebra|universal
enveloping algebra]] is equivalent to the graph topology defined by the
powers of \(1+\overline{\Delta_\pi}\).

## Dependence on choices

The displayed operator depends on the chosen basis, or equivalently on a
choice of [[linear-algebra/inner-product|inner product]] on the Lie algebra. Different choices yield
equivalent regularity scales and the same space \(H^\infty\), but they need
not yield the same operator. Unless the inner product is
\(\operatorname{Ad}(G)\)-invariant, the quadratic element
\(-\sum_jX_j^2\) is not central in the universal enveloping algebra and
\(\Delta_\pi\) need not commute with the representation.

## Analytic vectors and Nelson's theorem

Vectors analytic for \(\overline{\Delta_\pi}\) are [[lie-groups/analytic-vector-unitary-representation|analytic vectors]] for the
[[algebra-representation-theory/group-representation|group representation]]: their [[fiber-bundles/orbit-map|orbit maps]] \(g\mapsto\pi(g)v\) are real analytic
near the identity. Nelson's heat-kernel argument produces a dense supply of
such vectors. This converts an infinite family of infinitesimal generators
into a single elliptic regularity problem and is a key ingredient in criteria
for integrating representations of a Lie algebra to unitary representations
of a Lie group.

## Terminological warning

The Nelson Laplacian is attached to a representation and a Lie-algebra basis.
It should not automatically be identified with a geometric
Laplace–Beltrami operator or with a Casimir operator. In special
representations these operators can be related, but the identifications
require additional invariant geometric structure.

## References

1. Edward Nelson, “Analytic Vectors,” *Annals of Mathematics* 70 (1959), 572–615. [DOI record](https://doi.org/10.2307/1970331). Relevant: the Laplacian criterion, essential self-adjointness, and analytic vectors.
2. Roe Goodman, “Analytic and Entire Vectors for Representations of Lie Groups,” *Transactions of the American Mathematical Society* 143 (1969), 55–76. [DOI record](https://doi.org/10.1090/S0002-9947-1969-0248285-6). Relevant: analytic-vector regularity for Lie-group representations.
