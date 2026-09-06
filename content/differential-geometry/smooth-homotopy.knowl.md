+++
id = "differential-geometry/smooth-homotopy"
title = "Smooth homotopy"
kind = "definition"
summary = "A smooth homotopy is a smoothly parameterized one-parameter deformation between smooth maps."
aliases = ["homotopy through smooth maps"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/smooth-manifold", "fiber-bundles/smooth-map", "differential-geometry/smooth-map-of-manifolds-with-boundary", "differential-geometry/product-manifold", "differential-geometry/manifold-with-boundary", "shared-foundations/equivalence-relation"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) and \(N\) be [[fiber-bundles/smooth-manifold|smooth manifolds]] without boundary, and let \(f_0,f_1:M\to N\) be [[fiber-bundles/smooth-map|smooth maps]]. A **smooth homotopy** from \(f_0\) to \(f_1\) is a [[differential-geometry/smooth-map-of-manifolds-with-boundary|smooth map in the manifold-with-boundary sense]]
\[
F:M\times[0,1]\longrightarrow N
\]
such that \(F(x,0)=f_0(x)\) and \(F(x,1)=f_1(x)\) for every \(x\in M\). Here the [[differential-geometry/product-manifold|product]] \(M\times[0,1]\) has its standard [[differential-geometry/manifold-with-boundary|smooth manifold-with-boundary]] structure, and smoothness includes smooth extension in the interval direction at the endpoints. Smooth homotopy is an [[shared-foundations/equivalence-relation|equivalence relation]] on smooth maps and is the differential-category refinement of continuous homotopy.

## Homotopy formula for differential forms

Write \(F_t(x)=F(x,t)\). Integration in the interval direction defines an operator \(K:\Omega^k(N)\to\Omega^{k-1}(M)\) satisfying
\[
F_1^*-F_0^*=dK+Kd.
\]
Thus the two pullbacks of [[differential-geometry/de-rham-complex|de Rham complexes]] are cochain-homotopic and induce the same map on [[fiber-bundles/de-rham-cohomology-group|de Rham cohomology]]. This is the smooth homotopy-invariance mechanism used throughout de Rham theory.

## Examples and distinctions

If \(f:M\to N\) is constant along a smooth path in \(N\), that path gives a smooth homotopy between the corresponding constant maps. A [[differential-geometry/smooth-isotopy|smooth isotopy]] is stronger than a smooth homotopy: it requires each time slice to remain in a specified class, commonly diffeomorphisms or embeddings. A general smooth homotopy imposes no such condition on the slices.

## Conventions and scope

Some authors require a homotopy to be constant for \(t\) near \(0\) and \(1\), especially when homotopies will be concatenated smoothly. That is an additional collar convention, not part of the basic definition. If \(M\) itself has boundary, \(M\times[0,1]\) naturally has corners, so the ambient smooth category must be enlarged or the definition phrased using smooth extension on a neighborhood.

## References

1. Loring W. Tu, *An Introduction to Manifolds*, 2nd ed., Springer, 2011. [DOI record](https://doi.org/10.1007/978-1-4419-7400-6). Relevant: smooth homotopy and the homotopy formula in de Rham theory.
2. Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology*, Springer, 1982. [DOI record](https://doi.org/10.1007/978-1-4757-3951-0). Relevant: Chapter I, homotopy operators and de Rham theory.
