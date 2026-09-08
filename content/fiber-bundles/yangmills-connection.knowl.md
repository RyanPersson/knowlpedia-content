+++
id = "fiber-bundles/yangmills-connection"
title = "Yang–Mills connection"
kind = "knowl"
summary = "A principal connection satisfying the Yang–Mills equation."
aliases = ["yangmills-connection", "Yang–Mills connection"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/yangmills-connection.md"
prerequisites = ["differential-geometry/riemannian-manifold", "fiber-bundles/principal-connection", "fiber-bundles/yangmills-equation", "fiber-bundles/curvature"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(P\to M\) be a principal \(G\)-bundle over an oriented [[differential-geometry/riemannian-manifold|Riemannian manifold]].

A [[fiber-bundles/principal-connection|principal connection]] \(A\) on \(P\) is called a **Yang–Mills connection** if it satisfies the [[fiber-bundles/yangmills-equation|Yang–Mills equation]]
\[
d_A(*F_A)=0,
\]
where \(F_A\) is its [[fiber-bundles/curvature|curvature]].

## Variational interpretation

If the Lie algebra carries an Ad-invariant positive-definite inner product, the equation is equivalent to being a critical point of the [[fiber-bundles/yangmills-functional|Yang–Mills functional]] on a closed base. For a noncompact base, assume finite energy and use compactly supported variations; with boundary, impose boundary conditions or keep variations away from the boundary.

## Examples
1. **Flat connections.** Any flat connection is Yang–Mills, since its curvature vanishes.
2. **Anti-self-dual connections.** On an oriented 4-manifold, ASD (or SD) connections are Yang–Mills; these are the basic instanton solutions in [[fiber-bundles/gauge-theory|gauge theory]].
3. **Constant curvature on surfaces.** On a closed oriented surface, the Yang–Mills equation says that the curvature coefficient \(*F_A\) is covariantly constant. For an irreducible connection this coefficient is central; for reducible connections it may lie in a larger holonomy centralizer.
