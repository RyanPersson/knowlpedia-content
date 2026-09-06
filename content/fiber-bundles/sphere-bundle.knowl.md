+++
id = "fiber-bundles/sphere-bundle"
title = "Sphere bundle"
kind = "definition"
summary = "The fiber bundle of unit vectors in a positive-rank vector bundle equipped with a bundle metric."
aliases = ["unit sphere bundle", "spherical bundle"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/vector-bundle", "fiber-bundles/bundle-metric", "fiber-bundles/smooth-fiber-bundle", "fiber-bundles/typical-fiber"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(E\to M\) be a positive-rank real [[fiber-bundles/vector-bundle|vector bundle]] with [[fiber-bundles/bundle-metric|bundle metric]] \(g\). Its **unit sphere bundle** is
\[
S(E)=\{v\in E:g(v,v)=1\},
\]
with projection obtained by restricting \(E\to M\). If \(E\) has rank \(r\), then \(S(E)\to M\) is a [[fiber-bundles/smooth-fiber-bundle|smooth fiber bundle]] with [[fiber-bundles/typical-fiber|typical fiber]] \(S^{r-1}\). In a local orthonormal trivialization it is identified with \(U\times S^{r-1}\). Thus the metric selects a smooth unit sphere in each vector-space fiber, while the bundle's transition data describes how those spheres are glued.

## Basic properties

The closed unit disk bundle
\[
D(E)=\{v\in E:g(v,v)\leq 1\}
\]
is a bundle with fiber the closed disk \(D^r\), and its fiberwise boundary is \(S(E)\). The antipodal map \(v\mapsto-v\) defines a free involution on every sphere bundle.

Different bundle metrics on a fixed vector bundle yield isomorphic sphere bundles. One may construct a fiberwise positive automorphism carrying one metric to the other, so the isomorphism type depends on \(E\), not on the particular metric used to draw its unit spheres.

## Examples

For the trivial bundle \(M\times\mathbb R^r\), the sphere bundle is \(M\times S^{r-1}\).

For a [[differential-geometry/riemannian-manifold|Riemannian manifold]] \(M\), the sphere bundle of the [[fiber-bundles/tangent-bundle|tangent bundle]] is the unit tangent bundle. Its points are unit tangent vectors.

If \(L\) is a [[fiber-bundles/line-bundle|real line bundle]], then \(S(L)\to M\) has fiber \(S^0=\{-1,1\}\) and is a two-sheeted covering. For the Möbius line bundle this covering is connected and nontrivial.

A Hermitian complex bundle of complex rank \(n\), viewed with its underlying real metric, has unit sphere fibers \(S^{2n-1}\).

## Conventions and scope

Some authors use “sphere bundle” for any fiber bundle whose fiber is a sphere, whether or not it arises from a vector bundle. Others use it for the fiberwise one-point compactification of \(E\), whose fiber is \(S^r\), rather than for \(S(E)\), whose fiber is \(S^{r-1}\).

**Warning.** The metric unit sphere bundle, the principal bundle of orthonormal frames, and the projectivization of \(E\) are related but distinct bundles.

## References

1. D. Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-4008-0). Relevant: chapter 3, sphere and disk bundles associated to vector bundles.
