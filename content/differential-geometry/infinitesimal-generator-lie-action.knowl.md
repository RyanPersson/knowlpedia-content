+++
id = "differential-geometry/infinitesimal-generator-lie-action"
title = "Infinitesimal generator of a Lie group action"
kind = "definition"
summary = "An infinitesimal generator is the vector field obtained by differentiating a one-parameter subgroup acting on a manifold."
aliases = ["fundamental vector field", "infinitesimal action"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(G\) act smoothly on \(M\) from the left through a [[fiber-bundles/smooth-action-of-a-lie-group-on-a-manifold|smooth Lie group action]], and let \(\mathfrak{g}\) be the [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra of \(G\)]]. For \(\xi\in\mathfrak{g}\), its **infinitesimal generator** is the [[fiber-bundles/vector-field|vector field]]
\[
\xi_M(p)=\left.\frac{d}{dt}\right|_{t=0}\exp(t\xi)\mathbin{\cdot}p.
\]
The resulting [[linear-algebra/linear-map|linear map]] \(\mathfrak{g}\to\mathfrak{X}(M)\), \(\xi\mapsto\xi_M\), is called the infinitesimal action. With this formula for a left action, it is a [[lie-groups/lie-algebra|Lie algebra]] antihomomorphism: \([\xi_M,\eta_M]=-[\xi,\eta]_M\).

## Flow and stabilizers

The vector field \(\xi_M\) is complete, and its flow is
\[
\operatorname{Fl}^{\xi_M}_t(p)=\exp(t\xi)\mathbin{\cdot}p.
\]
At a point \(p\), the evaluation map \(\xi\mapsto\xi_M(p)\) has kernel equal to the Lie algebra of the stabilizer \(G_p\). Its image is the [[differential-geometry/tangent-space|tangent space]] to the orbit through \(p\). The generators transform equivariantly:
\[
d(g\mathbin{\cdot})_p\bigl(\xi_M(p)\bigr)=(\operatorname{Ad}_g\xi)_M(g\mathbin{\cdot}p).
\]

## Left and right action conventions

For a right action, the same unsigned formula \(p\mathbin{\cdot}\exp(t\xi)\) produces a [[lie-groups/lie-algebra-homomorphism|Lie algebra homomorphism]]. For a left action, replacing \(\exp(t\xi)\) by \(\exp(-t\xi)\) also produces a homomorphism. Both conventions occur in geometry, so bracket signs in moment-map and equivariance formulas depend on the chosen definition; see [Marsden and Ratiu, §9.1](https://doi.org/10.1007/978-0-387-21792-5).

## Examples

For the left action of \(G\) on itself by left multiplication, \(\xi_G\) is the [[lie-groups/right-invariant-vector-field|right-invariant vector field]] with value \(\xi\) at the identity, explaining the antihomomorphism sign. For a linear representation \(G\to\operatorname{GL}(V)\), the generator is \(\xi_V(v)=d\rho(\xi)v\).

## References

1. J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2013. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 21.
2. J. E. Marsden and T. S. Ratiu, *Introduction to Mechanics and Symmetry*, 2nd ed., Springer, 1999. [DOI record](https://doi.org/10.1007/978-0-387-21792-5). Relevant: §9.1.
