+++
id = "differential-geometry/category-of-smooth-manifolds"
title = "Category of smooth manifolds"
kind = "definition"
summary = "The category whose objects are smooth manifolds and whose morphisms are smooth maps."
aliases = ["smooth-manifold category", "category of manifolds and smooth maps"]
domains = ["differential-geometry", "category-theory"]
section_mode = "progressive"
+++

The **category of smooth manifolds**, commonly denoted \(\mathbf{Man}\) or \(\mathbf{SmoothMan}\), is the [[algebra-category-theory/category|category]] whose objects are finite-dimensional [[fiber-bundles/smooth-manifold|smooth manifolds]] and whose morphisms \(M\to N\) are [[fiber-bundles/smooth-map|smooth maps]]. Composition is ordinary composition of functions, and the [[algebra-category-theory/identity-morphism|identity morphism]] on \(M\) is \(\operatorname{id}_M\). These operations are smooth and satisfy the [[algebra-category-theory/category-axioms|category axioms]]. The isomorphisms in this category are exactly the [[fiber-bundles/diffeomorphism|diffeomorphisms]]. This definition fixes the finite-dimensional smooth category, not a category of infinite-dimensional or singular spaces.

## Products and terminal object

The one-point manifold is a [[algebra-category-theory/terminal-object|terminal object]]. The [[shared-foundations/cartesian-product|Cartesian product]] \(M\times N\), with its product smooth structure and projection maps, is the [[algebra-category-theory/categorical-product|categorical product]]. The empty manifold is an [[algebra-category-theory/initial-object|initial object]] when it is admitted by the chosen manifold convention.

## Functorial constructions

Many geometric operations are [[algebra-category-theory/functor|functorial]]. The [[fiber-bundles/tangent-bundle|tangent bundle]] sends a smooth map to its differential, while differential forms are contravariant under pullback. The assignment \(M\mapsto C^\infty(M)\) from the [[differential-geometry/algebra-of-smooth-functions|algebra of smooth functions]] reverses arrows.

## Conventions and categorical limits

The category depends on whether manifolds may have boundary, whether dimensions may vary by [[topology/connected-component|connected component]], and whether the empty manifold is allowed. Even after fixing conventions, arbitrary set-theoretic fiber products need not be smooth manifolds; transverse fiber products are the standard well-behaved case. The basic categorical language is as in [Mac Lane, Chapter I](https://doi.org/10.1007/978-1-4757-4721-8), while the smooth setting follows [Lee, chapters on smooth manifolds and maps](https://doi.org/10.1007/978-1-4419-9982-5).

## References

1. Saunders Mac Lane, *Categories for the Working Mathematician*, 2nd ed., Springer, 1998. [DOI record](https://doi.org/10.1007/978-1-4757-4721-8). Relevant: Chapter I, categories, functors, and natural transformations.
2. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: smooth manifolds, smooth maps, products, and diffeomorphisms.
