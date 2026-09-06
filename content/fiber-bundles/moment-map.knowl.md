+++
id = "fiber-bundles/moment-map"
title = "Moment map"
kind = "knowl"
summary = "A map from a Hamiltonian Lie group action to the dual Lie algebra encoding infinitesimal symmetries of a symplectic form."
aliases = ["moment-map", "Moment map"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/moment-map.md"
prerequisites = ["fiber-bundles/lie-group"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] acting by symplectomorphisms on a manifold \(M\) equipped with a symplectic form \(\omega\) (a closed, nondegenerate 2-form), and let \(\mathfrak{g}\) be its Lie algebra.

For \(\xi\in\mathfrak{g}\), write \(\xi_M\) for the fundamental vector field on \(M\), using a fixed sign convention.

## Definition (Moment map)
A **moment map** for the action is a smooth map
\[
\mu\colon M \to \mathfrak{g}^*
\]
such that for every \(\xi\in\mathfrak{g}\),
\[
d\langle \mu,\xi\rangle \;=\; \iota_{\xi_M}\omega,
\]
where \(d\) is the [[fiber-bundles/exterior-derivative|exterior derivative]] and \(\iota_{\xi_M}\) denotes contraction by the vector field \(\xi_M\).

The action is **Hamiltonian** if it admits a moment map. Some conventions instead use a minus sign in the displayed identity, and many definitions additionally require \(\mu\) to be \(G\)-equivariant with respect to the coadjoint action.

If \(M\) is connected, any two moment maps satisfying the displayed identity differ by a constant in \(\mathfrak{g}^*\). If both are equivariant, that constant is fixed by the coadjoint action.

A useful reformulation is that in [[fiber-bundles/equivariant-cohomology|equivariant cohomology]] (Cartan model), the pair \((\omega,\mu)\) combines into an equivariantly closed degree-2 element.

## Examples
1. **Rotation of the plane.** For the standard counterclockwise \(S^1\)-action on \(\mathbb{R}^2\cong \mathbb{C}\), the unsigned left-action generator, and \(\omega=dx\wedge dy\), a moment map is \(\mu(z)=-\tfrac12|z|^2\) (identifying \((\mathfrak{u}(1))^*\cong \mathbb{R}\)).
2. **Height on the 2-sphere.** For the standard rotation action of \(S^1\) on \(S^2\) around the vertical axis with the area form, a moment map is the height function (up to an additive constant).
3. **[[differential-geometry/cotangent-lift|Cotangent lift]].** If \(G\) acts on a manifold \(Q\), the induced action on \(T^*Q\) with its canonical symplectic form is Hamiltonian, with moment map \(\mu(q,p)(\xi)=p(\xi_Q(q))\).
