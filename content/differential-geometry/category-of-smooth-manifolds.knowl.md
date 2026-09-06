+++
id = "differential-geometry/category-of-smooth-manifolds"
title = "Category of smooth manifolds"
kind = "definition"
summary = "The category whose objects are smooth manifolds and whose morphisms are smooth maps."
aliases = ["smooth-manifold category", "category of manifolds and smooth maps", "Diff", "category Diff", "category of smooth manifolds and smooth maps"]
domains = ["differential-geometry", "category-theory"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/category", "fiber-bundles/smooth-manifold", "fiber-bundles/smooth-map"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

The **category of smooth manifolds**, denoted \(\mathbf{Man}\), has smooth
manifolds as objects and [[fiber-bundles/smooth-map|smooth maps]] as
morphisms. Identity maps are smooth, and composites of smooth maps are
smooth, so these data form a [[algebra-category-theory/category|category]].
The convention here allows disconnected manifolds, provided their component
dimensions are globally bounded.

## Categorical properties

An isomorphism in \(\mathbf{Man}\) is exactly a
[[fiber-bundles/diffeomorphism|diffeomorphism]]: a smooth map with a smooth
inverse. The product manifold is a categorical product, and a one-point
manifold is terminal.

## Related structures

The [[differential-geometry/category-of-complex-manifolds|category of complex
manifolds]] forgets complex charts to give a faithful functor to \(\mathbf{Man}\),
while the [[differential-geometry/category-of-symplectic-manifolds|category of
symplectic manifolds]] uses smooth manifolds with symplectic forms as objects
and form-preserving smooth maps as morphisms. The maximal subgroupoid of
\(\mathbf{Man}\) keeps the same objects and only diffeomorphisms.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012.
   [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapters 1–2, smooth manifolds and smooth maps.
