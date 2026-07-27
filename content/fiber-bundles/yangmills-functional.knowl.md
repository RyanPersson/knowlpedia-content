+++
id = "fiber-bundles/yangmills-functional"
title = "Yang–Mills functional"
kind = "knowl"
summary = "The curvature energy of a connection, defined as one half of the squared L² norm of its curvature."
aliases = ["yangmills-functional", "Yang–Mills functional"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/yangmills-functional.md"
+++

Let $M$ be a compact oriented Riemannian manifold without boundary, let $G$ be a Lie group with an $\mathrm{Ad}$-invariant inner product on its Lie algebra, and let $\pi:P\to M$ be a [[fiber-bundles/principal-g-bundle|principal $G$-bundle]].

For a [[fiber-bundles/principal-connection|principal connection]] $A$ on $P$, with [[fiber-bundles/curvature|curvature]] $F_A\in\Omega^2(M;\operatorname{Ad}(P))$, the **Yang–Mills functional** is
$$
\operatorname{YM}(A)=\frac12\int_M |F_A|^2\,\operatorname{vol}_g
=\frac12\int_M\langle F_A\wedge *F_A\rangle .
$$

Here $*$ is the Hodge star, and the pointwise norm and pairing use the Riemannian metric and the chosen inner product on the Lie algebra.

## Properties

The functional is invariant under gauge transformations of $P$. Its critical points are the [[fiber-bundles/yangmills-connection|Yang–Mills connections]], characterized by the [[fiber-bundles/yangmills-equation|Yang–Mills equation]].

## Examples
1. **Flat connections.** If $F_A=0$, then $\operatorname{YM}(A)=0$, the minimum possible value.
2. **Abelian case (Maxwell energy).** For $G=U(1)$, the curvature is an ordinary closed $2$-form, and $\operatorname{YM}(A)$ reduces to the classical electromagnetic energy $\frac12\int_M|F|^2\,\operatorname{vol}_g$.
3. **Four dimensions and self-duality.** On an oriented $4$-manifold, connections with self-dual or anti-self-dual curvature minimize $\operatorname{YM}$ within their topological class: the functional splits into a topological term plus a nonnegative remainder.
