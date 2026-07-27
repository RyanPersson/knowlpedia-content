+++
id = "differential-geometry/primitive-cohomology"
title = "Primitive cohomology"
kind = "definition"
summary = "The kernel of the appropriate power of the Lefschetz operator on the cohomology of a compact Kähler manifold."
aliases = ["primitive part of cohomology"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(X\) be a compact [[differential-geometry/kahler-manifold|Kähler manifold]] of complex dimension \(n\), and let \(L\) be the [[differential-geometry/lefschetz-operator|Lefschetz operator]] determined by its [[differential-geometry/kahler-class|Kähler class]]. For \(0\leq k\leq n\), the **primitive cohomology in degree \(k\)** is
\[
P^k(X,\mathbb C)
=\ker\!\left(L^{\,n-k+1}:H^k(X,\mathbb C)\longrightarrow
H^{2n-k+2}(X,\mathbb C)\right).
\]
Its component of bidegree \((p,q)\), where \(p+q=k\), is
\(P^{p,q}(X)=P^k(X,\mathbb C)\cap H^{p,q}(X)\). Thus primitiveness is relative to the chosen Kähler class; it is not merely a property of the underlying cohomology group. Higher-degree classes are described by Lefschetz powers of primitive classes in degrees at most \(n\).

## Equivalent harmonic description

Choose the [[differential-geometry/kahler-metric|Kähler metric]] determined by the [[differential-geometry/kahler-form|Kähler form]], and represent a class by its unique [[differential-geometry/harmonic-differential-form|harmonic form]]. The class is primitive exactly when this representative is annihilated by the adjoint Lefschetz operator \(\Lambda\). This identifies the cohomological kernel above with the pointwise notion of a primitive harmonic form [Voisin, §6.2, Proposition 6.24](https://doi.org/10.1017/CBO9780511615344).

## Lefschetz decomposition

The [[differential-geometry/hard-lefschetz-theorem|hard Lefschetz theorem]] yields the direct-sum decomposition
\[
H^k(X,\mathbb C)
=\bigoplus_{r\geq \max(0,k-n)}L^rP^{k-2r}(X,\mathbb C).
\]
Every cohomology class is therefore uniquely assembled from primitive classes and powers of the Kähler class. The decomposition respects bidegree because \(L\) has type \((1,1)\); see [Voisin, §6.2, Theorem 6.25](https://doi.org/10.1017/CBO9780511615344).

## Examples and scope

On [[algebraic-geometry-foundations/projective-space|projective space]] \(\mathbb{CP}^n\), the only primitive cohomology is \(P^0\): every positive even-degree generator is a positive power of the Kähler class. By contrast, the middle cohomology of a projective hypersurface can contain a substantial primitive summand.

**Warning.** Some authors call a differential form primitive whenever \(\Lambda\alpha=0\), without requiring harmonicity. Such forms need not define primitive cohomology classes unless they are closed and their harmonic representatives remain primitive.

## References

1. Claire Voisin, *Hodge Theory and Complex Algebraic Geometry I*, Cambridge Studies in Advanced Mathematics 76, Cambridge University Press, 2002. [Publisher record](https://doi.org/10.1017/CBO9780511615344). Relevant: §6.2, especially Proposition 6.24 and Theorem 6.25.
2. Daniel Huybrechts, *Complex Geometry: An Introduction*, Springer, 2005. [Publisher record](https://doi.org/10.1007/b137952). Relevant: Chapter 3, the Lefschetz decomposition and primitive cohomology.
