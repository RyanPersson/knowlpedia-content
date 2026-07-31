+++
id = "differential-geometry/category-of-smooth-manifolds"
title = "Category of smooth manifolds"
kind = "definition"
summary = "The category whose objects are smooth manifolds and whose morphisms are smooth maps."
aliases = ["smooth-manifold category", "category of manifolds and smooth maps"]
domains = ["differential-geometry", "category-theory"]
section_mode = "progressive"
+++

The **category of smooth manifolds**, commonly denoted \(\mathbf{Man}\) or
\(\mathbf{SmoothMan}\), is the [[algebra-category-theory/category|category]]
whose objects are finite-dimensional Hausdorff second-countable
[[fiber-bundles/smooth-manifold|smooth manifolds without boundary]] and whose
morphisms \(M\to N\) are [[fiber-bundles/smooth-map|smooth maps]]. This is
the house convention on this page. Disconnected objects are allowed, but
their dimensions are globally bounded; manifolds with boundary, corners,
infinite-dimensional manifolds, and singular spaces belong to separately
named categories.

Composition is ordinary composition of functions, and the
[[algebra-category-theory/identity-morphism|identity morphism]] on \(M\) is
\(\operatorname{id}_M\). These operations are smooth and satisfy the
[[algebra-category-theory/category-axioms|category axioms]]. The isomorphisms
in this category are exactly the
[[fiber-bundles/diffeomorphism|diffeomorphisms]].

## The category and its core

\(\mathbf{Man}\) contains all smooth maps, including constant maps,
embeddings, submersions, and maps that are not invertible. Retaining the same
objects but only the diffeomorphisms gives the
[[differential-geometry/diffeomorphism-groupoid-of-smooth-manifolds|
diffeomorphism groupoid]]
\(\mathbf{Man}^{\simeq}\), the maximal subgroupoid or core of
\(\mathbf{Man}\); in general this construction is the
[[algebra-category-theory/core-of-a-category|core of a category]].

These categories answer different questions. The core organizes manifolds up
to diffeomorphism and records their automorphism groups. The full category
\(\mathbf{Man}\) also supports functors whose behavior on noninvertible maps
is essential. Therefore the common phrase “manifolds with diffeomorphisms as
morphisms” describes \(\mathbf{Man}^{\simeq}\), not the usual
smooth-manifold category.

## Products and terminal object

The one-point manifold is a [[algebra-category-theory/terminal-object|terminal object]]. The [[shared-foundations/cartesian-product|Cartesian product]] \(M\times N\), with its product smooth structure and projection maps, is the [[algebra-category-theory/categorical-product|categorical product]]. The empty manifold is an [[algebra-category-theory/initial-object|initial object]] when it is admitted by the chosen manifold convention.

## Functorial constructions

Many geometric operations are [[algebra-category-theory/functor|functorial]]. The [[fiber-bundles/tangent-bundle|tangent bundle]] sends a smooth map to its differential, while differential forms are contravariant under pullback. The assignment \(M\mapsto C^\infty(M)\) from the [[differential-geometry/algebra-of-smooth-functions|algebra of smooth functions]] reverses arrows. When the full
[[differential-geometry/c-infinity-ring|\(C^\infty\)-ring]] structure is
retained, this functor is
[[differential-geometry/smooth-maps-from-smooth-function-algebras|fully
faithful onto its essential image]].

## Categorical limits

The empty manifold may be included as an
[[algebra-category-theory/initial-object|initial object]]; statements whose
algebraic conventions exclude the zero ring will say so separately.
Arbitrary set-theoretic fiber products need not be smooth manifolds;
transverse fiber products are the standard well-behaved case. The basic

## References

1. Saunders Mac Lane, *Categories for the Working Mathematician*, 2nd ed., Springer, 1998. [DOI record](https://doi.org/10.1007/978-1-4757-4721-8). Relevant: Chapter I, categories, functors, and natural transformations.
2. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: smooth manifolds, smooth maps, products, and diffeomorphisms.
