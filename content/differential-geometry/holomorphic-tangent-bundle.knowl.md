+++
id = "differential-geometry/holomorphic-tangent-bundle"
title = "Holomorphic tangent bundle"
kind = "definition"
summary = "The holomorphic vector bundle whose fibers are the complex tangent spaces of a complex manifold."
aliases = ["complex tangent bundle", "holomorphic tangent sheaf"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/complex-manifold", "differential-geometry/holomorphic-vector-bundle", "differential-geometry/complexified-tangent-bundle-splitting", "differential-geometry/almost-complex-structure", "linear-algebra/complexification", "fiber-bundles/tangent-bundle"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(X\) be a [[differential-geometry/complex-manifold|complex manifold]] of complex dimension \(n\). Its **holomorphic tangent bundle** \(T^{1,0}X\to X\) is the rank-\(n\) [[differential-geometry/holomorphic-vector-bundle|holomorphic vector bundle]] obtained by gluing the coordinate bundles with the complex Jacobian matrices of holomorphic coordinate changes. Its fiber at \(x\) is the complex tangent space \(T_x^{1,0}X\). Under the [[differential-geometry/complexified-tangent-bundle-splitting|type decomposition]], it is the \(i\)-eigenbundle of the complexified [[differential-geometry/almost-complex-structure|almost-complex structure]] and is a direct summand of the [[linear-algebra/complexification|complexification]] of the underlying real [[fiber-bundles/tangent-bundle|tangent bundle]].

## Local frames and sections

Holomorphic coordinates \(z^1,\ldots,z^n\) give a local holomorphic frame
\[
\frac{\partial}{\partial z^1},\ldots,\frac{\partial}{\partial z^n}.
\]
A [[differential-geometry/holomorphic-section|holomorphic section]] of \(T^{1,0}X\) is a holomorphic [[fiber-bundles/vector-field|vector field]], locally \(\sum_j a^j(z)\partial/\partial z^j\) with holomorphic coefficients. These sections form the holomorphic tangent sheaf.

## Duality and functoriality

The holomorphic dual of \(T^{1,0}X\) is the [[differential-geometry/holomorphic-cotangent-bundle|holomorphic cotangent bundle]] \(\Omega_X^1\). A [[differential-geometry/holomorphic-map|holomorphic map]] \(f:X\to Y\) has a complex-linear differential
\[
df:T^{1,0}X\longrightarrow f^*T^{1,0}Y,
\]
which is a [[differential-geometry/holomorphic-vector-bundle-morphism|holomorphic vector-bundle morphism]]. This construction is compatible with composition.

## Conventions and scope

Some authors write \(T_X\) for the holomorphic bundle or its sheaf of holomorphic sections. It is not the same object as the underlying real tangent bundle \(TX\), whose real rank is \(2n\), nor as the full complexification \(TX\otimes_{\mathbb R}\mathbb C=T^{1,0}X\oplus T^{0,1}X\). The identification with an eigenbundle uses the integrable complex structure.

## References

1. D. Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: §2.2, holomorphic tangent and cotangent bundles.
2. R. O. Wells Jr., *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008. [DOI record](https://doi.org/10.1007/978-0-387-73892-5). Relevant: Chapter I, §2, complex tangent bundles.
