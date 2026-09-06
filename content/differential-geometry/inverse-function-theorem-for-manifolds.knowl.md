+++
id = "differential-geometry/inverse-function-theorem-for-manifolds"
title = "Inverse function theorem for manifolds"
kind = "theorem"
summary = "A smooth map whose differential is invertible at a point is a diffeomorphism between suitable neighborhoods of that point and its image."
aliases = ["manifold inverse function theorem", "local inverse theorem"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/smooth-map", "fiber-bundles/smooth-manifold", "fiber-bundles/differential-of-a-smooth-map", "algebraic-geometry-foundations/local-diffeomorphism"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(F:M\to N\) be a [[fiber-bundles/smooth-map|smooth map]] between finite-dimensional [[fiber-bundles/smooth-manifold|smooth manifolds]] without boundary, and let \(p\in M\). If the [[fiber-bundles/differential-of-a-smooth-map|differential]]
\[
dF_p:T_pM\longrightarrow T_{F(p)}N
\]
is a linear isomorphism, then there are open neighborhoods \(U\) of \(p\) and \(V\) of \(F(p)\) such that \(F|_U:U\to V\) is a diffeomorphism. Equivalently, \(F\) is a [[algebraic-geometry-foundations/local-diffeomorphism|local diffeomorphism]] at \(p\). Conversely, any smooth map that is a local diffeomorphism at \(p\) has invertible differential there.

## Why the manifold statement follows

Choose [[fiber-bundles/smooth-chart|smooth charts]] around \(p\) and \(F(p)\). In coordinates, the differential of the representative of \(F\) is invertible at the coordinate of \(p\). The Euclidean [[shared-foundations/inverse-function|inverse function]] theorem supplies mutually inverse smooth maps on smaller open sets; conjugating them by the charts gives the required manifold neighborhoods. This also shows that the statement is independent of the chosen charts.

## Consequences

Invertibility of \(dF_p\) forces \(\dim M=\dim N\). Since invertible [[linear-algebra/linear-map|linear maps]] form an open subset, \(dF_q\) remains invertible for all \(q\) sufficiently near \(p\). Thus the set on which \(F\) is a local diffeomorphism is open. A bijective local diffeomorphism is a diffeomorphism, because its locally defined smooth inverses agree with the set-theoretic inverse.

## Scope and near misses

The theorem is local and does not imply global injectivity: the [[fiber-bundles/exponential-map|exponential map]] \(\mathbb{R}\to S^1\), \(t\mapsto e^{it}\), has invertible differential everywhere but is not one-to-one. For manifolds with boundary, invertibility of the tangent map alone does not give this conclusion at [[differential-geometry/boundary-and-interior-of-a-manifold|boundary points]] without additional hypotheses controlling the boundary.

## References

1. J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2013. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 4.
2. L. W. Tu, *An Introduction to Manifolds*, 2nd ed., Springer, 2011. [DOI record](https://doi.org/10.1007/978-1-4419-7400-6). Relevant: §6.7 and Remark 8.12.
