+++
id = "differential-geometry/embedded-submanifold"
title = "Embedded submanifold"
kind = "definition"
summary = "A subset of a smooth manifold that is locally a coordinate plane in ambient smooth charts."
aliases = ["regular submanifold", "smoothly embedded submanifold", "smooth submanifold"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(M\) be an \(n\)-dimensional [[fiber-bundles/smooth-manifold|smooth manifold]]. A subset \(S\subseteq M\) is a \(k\)-dimensional **embedded submanifold** if every \(p\in S\) has a [[fiber-bundles/smooth-chart|smooth chart]] \((U,\varphi)\) of \(M\) such that
\[
\varphi(U\cap S)=\varphi(U)\cap(\mathbb R^k\times\{0\}) .
\]
The set \(S\) is given the [[topology/subspace-topology|subspace topology]] and the smooth structure induced by these slice charts. With this structure the inclusion \(S\hookrightarrow M\) is a [[fiber-bundles/smooth-embedding|smooth embedding]], and the codimension of \(S\) is \(n-k\).

## Equivalent intrinsic formulation

Equivalently, \(S\) is a smooth manifold with its subspace topology such that its inclusion into \(M\) is a smooth embedding. The local coordinate-plane condition determines this smooth structure uniquely. A map \(f:N\to S\) from a smooth manifold is smooth exactly when the composite \(N\to S\hookrightarrow M\) is smooth [Lee, Chapter 5](https://doi.org/10.1007/978-1-4419-9982-5).

## Standard constructions

Open subsets of \(M\) are embedded submanifolds of dimension \(n\). Coordinate planes, spheres, and graphs of [[fiber-bundles/smooth-map|smooth maps]] are basic examples. More generally, the level set of a smooth map at a [[fiber-bundles/regular-value|regular value]] is an embedded submanifold; the derivative determines its [[differential-geometry/tangent-space|tangent spaces]] as kernels.

## Embedded versus immersed

An injective [[fiber-bundles/smooth-immersion|smooth immersion]] need not be an embedding because its inverse onto the image may fail to be continuous for the subspace topology. Embeddedness therefore controls both the local differential behavior and the topology inherited from the ambient manifold. Some texts reserve “submanifold” for the embedded notion, while others distinguish embedded and [[differential-geometry/immersed-submanifold|immersed submanifolds]] explicitly.

## References

1. J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [Springer DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 5.
2. L. W. Tu, *An Introduction to Manifolds*, 2nd ed., Springer, 2011. [Springer DOI record](https://doi.org/10.1007/978-1-4419-7400-6). Relevant: Chapter 8.
