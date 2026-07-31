+++
id = "differential-geometry/quaternion-kahler-manifold"
title = "Quaternion-Kähler manifold"
kind = "definition"
summary = "A Riemannian manifold of dimension at least eight whose holonomy is contained in Sp(n)Sp(1)."
aliases = ["quaternionic-Kähler manifold"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

For \(n\geq2\), a **quaternion-Kähler manifold** is a [[differential-geometry/riemannian-manifold|Riemannian manifold]] \((M^{4n},g)\) whose [[fiber-bundles/holonomy-group|holonomy group]] is contained in the [[lie-groups/compact-symplectic-product-group|group \(\operatorname{Sp}(n)\operatorname{Sp}(1)\)]]. Equivalently, \(M\) carries a rank-three subbundle \(Q\subseteq\operatorname{End}(TM)\), locally spanned by a quaternionic triple \(I,J,K\), such that \(g\) is [[differential-geometry/quaternionic-hermitian-manifold|quaternionic-Hermitian]] and the [[fiber-bundles/levicivita-connection-connection|Levi-Civita connection]] preserves \(Q\). It may rotate \(I,J,K\) rather than preserve each separately. The definition is Riemannian and does not assert that \(M\) is a complex or a [[differential-geometry/kahler-manifold|Kähler manifold]].

## Structure and consequences

The preserved bundle \(Q\) makes every quaternion-Kähler manifold of dimension at least eight a [[differential-geometry/quaternionic-manifold|quaternionic manifold]]. Its Levi-Civita connection induces a connection on \(Q\), and the associated fundamental four-form is parallel. Such metrics are Einstein; this is a holonomy consequence rather than an additional defining axiom under the higher-dimensional convention.

## Examples and nearby structures

Quaternionic projective space \(\mathbb H P^n\) with its standard metric is the compact positive-curvature model. Quaternionic hyperbolic space is the corresponding negative-curvature model. A [[differential-geometry/hyperkahler-manifold|hyperkähler manifold]] also satisfies the inclusive holonomy condition because \(\operatorname{Sp}(n)\subset\operatorname{Sp}(n)\operatorname{Sp}(1)\), but its Levi-Civita connection preserves a global triple and its [[differential-geometry/ricci-curvature|Ricci curvature]] vanishes.

Some authors reserve “quaternion-Kähler” for the nonzero-scalar-curvature case, thereby excluding hyperkähler manifolds; the core uses the inclusive holonomy convention of.

## Four-dimensional convention

When \(n=1\), \(\operatorname{Sp}(1)\operatorname{Sp}(1)=\operatorname{SO}(4)\), so the bare holonomy condition imposes no restriction on an oriented Riemannian four-manifold. Authors usually define a four-dimensional quaternion-Kähler manifold instead to be an Einstein self-dual manifold, with “self-dual” versus “anti-self-dual” depending on the orientation convention. This exceptional convention is not included in the core definition.

## References

1. Arthur L. Besse, *Einstein Manifolds*, Springer, 1987. [Springer DOI record](https://doi.org/10.1007/978-3-540-74311-8). Relevant: Chapter 14, especially Theorem 14.39.
2. Simon Salamon, “Quaternionic Kähler Manifolds,” *Inventiones Mathematicae* 67 (1982), 143–171. [DOI record](https://doi.org/10.1007/BF01393378). Relevant: pp. 143–145 for the holonomy groups and dimensional convention.
