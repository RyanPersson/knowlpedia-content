+++
id = "lie-groups/analytic-vector-unitary-representation"
title = "Analytic vector of a Lie-group representation"
kind = "definition"
summary = "A representation vector whose orbit map is real analytic near the identity of the Lie group."
aliases = ["analytic vector"]
domains = ["lie-groups", "functional-analysis"]
prerequisites = ["fiber-bundles/lie-group", "lie-groups/strongly-continuous-unitary-representation", "fiber-bundles/orbit-map", "lie-groups/derived-representation-on-smooth-vectors"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a finite-dimensional real [[fiber-bundles/lie-group|Lie group]] and \((\pi,\mathcal H)\) a [[lie-groups/strongly-continuous-unitary-representation|strongly continuous unitary representation]]. A vector \(v\in\mathcal H\) is an **analytic vector** if its [[fiber-bundles/orbit-map|orbit map]]
\[
G\longrightarrow\mathcal H,\qquad g\longmapsto\pi(g)v,
\]
is real analytic in a neighborhood of the identity, as a Hilbert-space-valued map. Equivalently, in local exponential coordinates its Taylor series, formed from iterated operators of the [[lie-groups/derived-representation-on-smooth-vectors|derived representation]], converges in norm to the orbit map near \(0\). Every analytic vector is smooth, but a smooth vector need not be analytic.

## Operator criterion

For a one-parameter group with self-adjoint generator \(A\), a vector \(v\) is analytic precisely when \(v\) lies in every domain \(\mathcal D(A^n)\) and
\[
\sum_{n=0}^{\infty}\frac{t^n}{n!}\lVert A^n v\rVert<\infty
\]
for some \(t>0\). For a Lie group, analogous factorial estimates for a basis of its [[lie-groups/lie-algebra|Lie algebra]] characterize analytic orbit maps. These estimates connect analytic vectors to [[lie-groups/nelson-analytic-vector-theorem|Nelson's analytic vector theorem]].

## Density and examples

[[lie-groups/nelson-analytic-vector-theorem|Nelson's analytic vector theorem]]
implies that analytic vectors are dense in the strongly continuous unitary
representation considered here; its proof uses heat-kernel regularization.

For translations of \(\mathbb R\) on \(L^2(\mathbb R)\), vectors whose Fourier transforms have a square-integrable exponential weight are analytic. A vector with only polynomial Fourier decay can be smooth while failing the factorial convergence test.

## Conventions and scope

**Warning.** An “entire vector” for one operator satisfies the displayed series for every \(t>0\), so it is stronger than being analytic and is not an alias here. Analyticity is also stronger than membership in the [[lie-groups/smooth-vector-unitary-representation|smooth-vector space]]. Local analyticity near the identity suffices because the representation action transports it to every point of \(G\).

## References

1. Edward Nelson, *Analytic vectors*, Annals of Mathematics 70 (1959), 572–615. [DOI record](https://doi.org/10.2307/1970331). Relevant: §§4–6 on analytic vectors for Lie-group representations and heat-kernel regularization.
2. Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics II: Fourier Analysis, Self-Adjointness*, Academic Press, 1975. [Publisher record](https://www.sciencedirect.com/book/9780125850025/methods-of-modern-mathematical-physics). Relevant: §X.6 on analytic vectors and essential self-adjointness.
