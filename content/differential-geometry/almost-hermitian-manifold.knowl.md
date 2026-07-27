+++
id = "differential-geometry/almost-hermitian-manifold"
title = "Almost-Hermitian manifold"
kind = "definition"
summary = "A smooth manifold with an almost-complex structure and a compatible Riemannian metric."
aliases = ["almost Hermitian manifold", "almost-Hermitian structure"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

An **almost-Hermitian manifold** is a triple \((M,J,g)\) in which \(M\) is a [[fiber-bundles/smooth-manifold|smooth manifold]], \(J\) is an [[differential-geometry/almost-complex-structure|almost-complex structure]], and \(g\) is a Riemannian metric satisfying
\[
g(JX,JY)=g(X,Y)
\]
for all tangent vectors \(X,Y\) at the same point. Equivalently, \(g\) is the real part of a [[fiber-bundles/hermitian-metric|Hermitian metric]] on the [[fiber-bundles/complex-vector-bundle|complex vector bundle]] \((TM,J)\). The associated fundamental \(2\)-form is
\[
\omega(X,Y)=g(JX,Y).
\]
It is smooth and nondegenerate, but it need not be closed.

## Compatible triples

Any two of \(J\), \(g\), and \(\omega\) determine the third when they satisfy the compatibility and positivity conditions. In particular,
\[
g(X,Y)=\omega(X,JY)
\]
for the sign convention in the core. The linear-algebra construction can be carried out smoothly, and every almost-complex manifold admits compatible metrics; see [Cannas da Silva, “Compatible Almost Complex Structures”](https://doi.org/10.1007/978-3-540-45330-7).

## Relationship to symplectic and complex geometry

If \(d\omega=0\), then \((M,\omega)\) is a [[differential-geometry/symplectic-manifold|symplectic manifold]] and the structure is called almost Kähler. If \(J\) is [[differential-geometry/integrable-almost-complex-structure|integrable]], the manifold is Hermitian. Requiring both integrability and \(d\omega=0\) gives a Kähler structure. Neither condition follows from almost-Hermitian compatibility alone.

## Examples and conventions

[[linear-algebra/euclidean-space|Euclidean space]] \(\mathbb R^{2n}\), with its standard complex structure and Euclidean metric, is almost Hermitian. More generally, a Hermitian metric on a [[differential-geometry/complex-manifold|complex manifold]] gives an almost-Hermitian structure on its underlying smooth manifold. Some authors define the [[differential-geometry/fundamental-form-almost-hermitian|fundamental form]] as \(g(X,JY)\), which is the negative of the convention used here.

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Springer, 2008. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: “Almost Complex Structures” and “Compatible Triples.”
2. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [DOI record](https://doi.org/10.1007/b137952). Relevant: chapter on Kähler manifolds and Hermitian structures.
