+++
id = "fiber-bundles/moment-map"
title = "Moment map"
kind = "knowl"
summary = "A map from a Hamiltonian Lie group action to the dual Lie algebra encoding infinitesimal symmetries of a symplectic form."
aliases = ["moment-map", "Moment map"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/moment-map.md"
+++

Let $G$ be a [[fiber-bundles/lie-group|Lie group]] acting by symplectomorphisms on a symplectic manifold $(M,\omega)$, and let $\mathfrak g$ be its Lie algebra. For $\xi\in\mathfrak g$, write $\xi_M$ for the fundamental vector field determined by a fixed sign convention.

A **moment map** for the action is a smooth map
$$
\mu\colon M \to \mathfrak{g}^*
$$
such that for every $\xi\in\mathfrak g$,
$$
d\langle \mu,\xi\rangle \;=\; \iota_{\xi_M}\omega,
$$
where $d$ is the [[fiber-bundles/exterior-derivative|exterior derivative]] and $\iota_{\xi_M}$ denotes contraction by $\xi_M$.

The action is **Hamiltonian** if it admits a moment map. Some conventions instead use a minus sign in the displayed identity, and many definitions also require $\mu$ to be equivariant for the coadjoint action.

## Remarks

If $M$ is connected, any two moment maps satisfying the displayed identity differ by a constant in $\mathfrak g^*$. If both are equivariant, that constant is fixed by the coadjoint action.

A useful reformulation is that in [[fiber-bundles/equivariant-cohomology|equivariant cohomology]] (Cartan model), the pair $(\omega,\mu)$ combines into an equivariantly closed degree-$2$ element.

## Examples
1. **Rotation of the plane.** For the $S^1$-action on $\mathbb{R}^2\cong\mathbb{C}$ by rotations and $\omega=dx\wedge dy$, a moment map is $\mu(z)=\tfrac12|z|^2$, with sign depending on the convention for the fundamental vector field.
2. **Height on the 2-sphere.** For the standard rotation action of $S^1$ on $S^2$ around the vertical axis with the area form, a moment map is the height function, up to sign and an additive constant.
3. **Cotangent lift.** If $G$ acts on a manifold $Q$, the induced action on $T^*Q$ with its canonical symplectic form is Hamiltonian, with moment map $\mu(q,p)(\xi)=p(\xi_Q(q))$, subject to the same sign convention.
