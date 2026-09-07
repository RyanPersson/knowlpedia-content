+++
id = "fiber-bundles/moment-map"
title = "Moment map"
kind = "knowl"
summary = "A map from a Hamiltonian Lie group action to the dual Lie algebra encoding infinitesimal symmetries of a symplectic form."
aliases = ["moment-map", "Moment map"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/moment-map.md"
prerequisites = ["differential-geometry/symplectic-lie-group-action", "lie-groups/lie-algebra-of-a-lie-group", "lie-groups/exponential-map-lie-group", "fiber-bundles/smooth-map", "fiber-bundles/exterior-derivative", "fiber-bundles/interior-product-contraction-x"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] with a [[differential-geometry/symplectic-lie-group-action|symplectic action]] on \((M,\omega)\), and let \(\mathfrak g\) be its [[lie-groups/lie-algebra-of-a-lie-group|Lie algebra]]. Write \(\mathfrak g^*=\operatorname{Hom}_{\mathbb R}(\mathfrak g,\mathbb R)\) for its linear dual.

For \(\xi\in\mathfrak g\), use the fundamental vector field \(\xi_M(x)=\left.\frac{d}{dt}\right|_{t=0}\exp(t\xi)\cdot x\), where \(\exp\) is the [[lie-groups/exponential-map-lie-group|exponential map]].

A **moment map** for the action is a [[fiber-bundles/smooth-map|smooth map]]
\[
\mu\colon M \to \mathfrak{g}^*
\]
such that for every \(\xi\in\mathfrak{g}\),
\[
d\langle \mu,\xi\rangle \;=\; \iota_{\xi_M}\omega,
\]
where \(d\) is the [[fiber-bundles/exterior-derivative|exterior derivative]] and \(\iota_{\xi_M}\) denotes [[fiber-bundles/interior-product-contraction-x|contraction]] by the vector field \(\xi_M\).

## Conventions and uniqueness

This definition does not impose equivariance. An equivariant moment map also satisfies \(\mu(gx)=\operatorname{Ad}_g^*\mu(x)\) for the [[fiber-bundles/coadjoint-action-of-a-lie-group|coadjoint action]]. The [[differential-geometry/hamiltonian-lie-group-action|Hamiltonian-action]] entry uses this stronger convention; some authors call an action Hamiltonian as soon as it has a moment map in the present sense. A different sign convention may replace the displayed identity by its negative.

If \(M\) is connected, any two moment maps satisfying the displayed identity differ by a constant in \(\mathfrak{g}^*\). If both are equivariant, that constant is fixed by the coadjoint action.

For an equivariant moment map, a useful reformulation is that in [[fiber-bundles/equivariant-cohomology|equivariant cohomology]] (Cartan model), the pair \((\omega,\mu)\) combines into an equivariantly closed degree-2 element.

## Examples
1. **Rotation of the plane.** For the standard counterclockwise \(S^1\)-action on \(\mathbb{R}^2\cong \mathbb{C}\), the unsigned left-action generator, and \(\omega=dx\wedge dy\), a moment map is \(\mu(z)=-\tfrac12|z|^2\) (identifying \((\mathfrak{u}(1))^*\cong \mathbb{R}\)).
2. **Height on the 2-sphere.** For the standard rotation action of \(S^1\) on \(S^2\) around the vertical axis with the area form, a moment map is the height function (up to an additive constant).
3. **[[differential-geometry/cotangent-lift|Cotangent lift]].** If \(G\) acts on a manifold \(Q\), the induced action on \(T^*Q\) with its canonical symplectic form is Hamiltonian, with moment map \(\mu(q,p)(\xi)=p(\xi_Q(q))\).
