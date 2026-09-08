+++
id = "fiber-bundles/good-cover"
title = "Good cover"
kind = "knowl"
summary = "An open cover whose nonempty finite intersections are contractible."
aliases = ["good-cover", "Good cover"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/good-cover.md"
prerequisites = ["topology/topological-space", "topology/open-cover", "topology/contractible-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a topological space (often a smooth manifold).

An open cover \(\{U_i\}_{i\in I}\) of \(X\) is a **good cover** if every nonempty finite intersection
\[
U_{i_0}\cap \cdots \cap U_{i_k}
\]
is [[topology/contractible-space|contractible]] (including the intersections consisting of a single cover member).

## Existence on manifolds

A smooth manifold admits good covers subordinate to any prescribed open cover, using sufficiently small strongly geodesically convex neighborhoods for a Riemannian metric. Arbitrary coordinate neighborhoods need not have contractible intersections.

## Applications

Good covers are especially useful because many global invariants can be computed from the combinatorics of the cover, and because they behave well with constructions built from local trivializations (for example, principal bundles and their transition functions).

## Examples
1. **Convex covers of \(\mathbb R^n\).**
   Any cover of \(\mathbb R^n\) by sufficiently small convex open sets (for instance, small Euclidean balls) is a good cover, since finite intersections of convex open sets are convex and hence contractible.

2. **A good cover of the circle.**
   \(S^1\) admits a good cover by three open arcs arranged so that all nonempty intersections are (possibly smaller) open arcs, hence contractible.

3. **A concrete nonexample.**
   Cover \(S^2\) by the complements of the north and south poles. Their intersection is the twice-punctured sphere, homotopy equivalent to \(S^1\), so it is not contractible; this two-set cover is not good.
