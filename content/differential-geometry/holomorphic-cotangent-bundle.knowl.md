+++
id = "differential-geometry/holomorphic-cotangent-bundle"
title = "Holomorphic cotangent bundle"
kind = "definition"
summary = "The holomorphic dual of the holomorphic tangent bundle of a complex manifold."
aliases = ["holomorphic one-form bundle", "holomorphic cotangent sheaf"]
domains = ["differential-geometry"]
section_mode = "progressive"
prerequisites = ["differential-geometry/complex-manifold", "differential-geometry/holomorphic-tangent-bundle", "differential-geometry/holomorphic-vector-bundle"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a [[differential-geometry/complex-manifold|complex manifold]]. Its **holomorphic cotangent bundle**, denoted \(T^{*1,0}X\) or \(\Omega_X^1\), is the holomorphic dual of the [[differential-geometry/holomorphic-tangent-bundle|holomorphic tangent bundle]] \(T^{1,0}X\). Thus it is a [[differential-geometry/holomorphic-vector-bundle|holomorphic vector bundle]] whose fiber at \(x\) is \((T_x^{1,0}X)^*\). Holomorphic coordinate functions \(z^1,\ldots,z^n\) give the local frame \(dz^1,\ldots,dz^n\), and changes of frame are the inverse transposes of the holomorphic Jacobian matrices. Its underlying smooth bundle is the \((1,0)\)-cotangent summand.

## Sections and pullback

[[differential-geometry/holomorphic-section|Holomorphic sections]] of \(\Omega_X^1\) are holomorphic one-forms. Locally they are sums \(\sum_j f_j(z)\,dz^j\) with holomorphic coefficients. A [[differential-geometry/holomorphic-map|holomorphic map]] \(f:X\to Y\) induces a pullback morphism
\[
f^*\Omega_Y^1\longrightarrow\Omega_X^1
\]
by precomposition with its differential.

## Exterior powers

The holomorphic bundle of \(p\)-forms is \(\Omega_X^p=\Lambda^p\Omega_X^1\). Its local sections are holomorphic \((p,0)\)-forms. If \(n=\dim_{\mathbb C}X\), the top exterior power
\[
K_X=\Lambda^n\Omega_X^1
\]
is the canonical [[differential-geometry/holomorphic-line-bundle|holomorphic line bundle]].

## Conventions and comparison

The notation \(\Omega_X^1\) may mean either the holomorphic vector bundle or its [[algebraic-geometry-foundations/sheaf|sheaf]] of holomorphic sections; context distinguishes them. The holomorphic cotangent bundle is not the full [[linear-algebra/complexification|complexification]] of the real [[fiber-bundles/cotangent-bundle|cotangent bundle]], which splits into \((1,0)\) and \((0,1)\) summands. It is the holomorphic refinement of the corresponding [[fiber-bundles/dual-vector-bundle|dual vector bundle]].

## References

1. D. Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: §2.2, holomorphic tangent and cotangent bundles.
2. R. O. Wells Jr., *Differential Analysis on Complex Manifolds*, 3rd ed., Springer, 2008. [DOI record](https://doi.org/10.1007/978-0-387-73892-5). Relevant: Chapter I, §2, complex cotangent bundles and forms.
