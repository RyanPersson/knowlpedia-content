+++
id = "differential-geometry/holomorphic-section"
title = "Holomorphic section"
kind = "definition"
summary = "A section of a holomorphic bundle that is holomorphic as a map into the total space."
aliases = ["analytic section", "holomorphic bundle section"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/holomorphic-vector-bundle", "differential-geometry/holomorphic-map", "fiber-bundles/section-of-a-fiber-bundle"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\pi:E\to X\) be a [[differential-geometry/holomorphic-vector-bundle|holomorphic vector bundle]]. A **holomorphic section** over an open set \(U\subseteq X\) is a [[differential-geometry/holomorphic-map|holomorphic map]] \(s:U\to E\) satisfying \(\pi\circ s=\operatorname{id}_U\); in particular, it is a [[fiber-bundles/section-of-a-fiber-bundle|section of the underlying smooth bundle]]. In a holomorphic trivialization \(E|_V\cong V\times\mathbb C^r\), the section has the form \(x\mapsto(x,s^1(x),\ldots,s^r(x))\), where all coefficient functions \(s^j\) are holomorphic. This local condition is independent of the chosen holomorphic trivialization.

## Sheaf of sections

Holomorphic sections restrict to smaller open sets and uniquely glue when they agree on overlaps. Hence \(U\mapsto\Gamma(U,E)\) is a [[algebraic-geometry-foundations/sheaf|sheaf]] and a module over the [[differential-geometry/sheaf-of-holomorphic-functions|sheaf of holomorphic functions]]. In a local holomorphic frame it is a [[algebra-modules/free-module|free module]] of rank \(r\).

## Zeros and trivializations

A rank-\(r\) bundle is holomorphically trivial over \(U\) exactly when it has \(r\) holomorphic sections that form a basis in every fiber. In particular, a [[differential-geometry/holomorphic-line-bundle|holomorphic line bundle]] is trivial exactly when it admits a nowhere-vanishing global holomorphic section. A nonzero holomorphic section of a [[fiber-bundles/line-bundle|line bundle]] may vanish, and its zero set carries analytic information.

## Comparison with smooth sections

Every holomorphic section is smooth, but a smooth section need not be holomorphic. In a holomorphic frame, the distinction is precisely whether its coefficient functions are holomorphic. This is stronger than pointwise complex-linearity, which is automatic for the selected vectors and imposes no differential condition.

## References

1. D. Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: §2.2, holomorphic bundles and their sections.
2. P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978. [DOI record](https://doi.org/10.1002/9781118032527). Relevant: Chapter 1, §1, sections of holomorphic bundles.
