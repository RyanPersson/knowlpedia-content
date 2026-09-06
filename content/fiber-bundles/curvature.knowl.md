+++
id = "fiber-bundles/curvature"
title = "Curvature"
kind = "knowl"
summary = "The infinitesimal obstruction to integrability of a connection's horizontal distribution."
aliases = ["curvature"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/curvature.md"
prerequisites = ["fiber-bundles/horizontal-distribution", "fiber-bundles/principal-connection", "fiber-bundles/principal-g-bundle", "fiber-bundles/connection-on-a-vector-bundle", "fiber-bundles/vector-bundle", "fiber-bundles/curvature-2-form-of-a-principal-connection", "fiber-bundles/curvature-of-a-vector-bundle-connection", "fiber-bundles/characteristic-class"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

In differential geometry, **curvature** is the infinitesimal obstruction to integrability of the [[fiber-bundles/horizontal-distribution|horizontal distribution]] determined by a connection.

The notion takes different but related forms depending on context:

1. **Principal bundles.** For a [[fiber-bundles/principal-connection|principal connection]] on a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]], the curvature is the [[fiber-bundles/curvature-2-form-of-a-principal-connection|curvature \(2\)-form]] \(\Omega \in \Omega^2(P;\mathfrak{g})\), defined by
   \[
   \Omega = d\omega + \tfrac{1}{2}[\omega \wedge \omega].
   \]

   In a local trivialization with gauge potential \(A\), this pulls back to the [[fiber-bundles/local-curvature-2-form|local curvature]] \(F = dA + \tfrac{1}{2}[A \wedge A]\).

2. **Vector bundles.** For a [[fiber-bundles/connection-on-a-vector-bundle|connection]] \(\nabla\) on a [[fiber-bundles/vector-bundle|vector bundle]], the curvature is the [[fiber-bundles/curvature-of-a-vector-bundle-connection|curvature endomorphism]] \(R^\nabla\), an \(\operatorname{End}(E)\)-valued \(2\)-form satisfying
   \[
   R^\nabla(X,Y)s = \nabla_X\nabla_Ys-\nabla_Y\nabla_Xs-\nabla_{[X,Y]}s.
   \]

3. **Frame bundles.** The [[fiber-bundles/curvature-2-form-in-a-frame|curvature in a frame]] relates the principal bundle and vector bundle viewpoints: a connection on a vector bundle induces a principal connection on its frame bundle, and their curvatures correspond.

A connection is [[fiber-bundles/flat-principal-connection|flat]] when its curvature vanishes. Flatness is equivalent to integrability of the horizontal distribution. For a flat connection, parallel transport depends only on the endpoint-preserving homotopy class of a path; it need not be independent of the path when the base has nontrivial fundamental group.

The curvature appears fundamentally in the [[fiber-bundles/chernweil-theorem-p-is-closed-and-its-de-rham-class-is-independent-of-connection|Chern–Weil theorem]], where invariant polynomials applied to the curvature yield [[fiber-bundles/characteristic-class|characteristic classes]].
