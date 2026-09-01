+++
id = "differential-geometry/poisson-algebra-smooth-functions"
title = "Poisson algebra of smooth functions"
kind = "definition"
summary = "The commutative algebra of smooth functions equipped with the Poisson bracket induced by a symplectic form."
aliases = ["classical observable algebra"]
domains = ["differential-geometry", "classical-mechanics"]
prerequisites = ["differential-geometry/symplectic-manifold", "differential-geometry/poisson-bracket-symplectic", "lie-groups/lie-algebra", "fiber-bundles/lie-bracket"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \((M,\omega)\) be a [[differential-geometry/symplectic-manifold|symplectic manifold]]. Its **Poisson algebra of smooth functions** is the real unital commutative algebra \(C^\infty(M,\mathbb R)\), with pointwise multiplication, together with the [[differential-geometry/poisson-bracket-symplectic|Poisson bracket]] \(\{-,-\}\). The bracket is real-bilinear and antisymmetric, satisfies the Jacobi identity, and obeys the Leibniz rule
\[
\{f,gh\}=\{f,g\}h+g\{f,h\}.
\]
Thus it is simultaneously a [[lie-groups/lie-algebra|Lie algebra]] and a commutative associative algebra, with the [[fiber-bundles/lie-bracket|Lie bracket]] acting as a derivation in either argument.

## Geometric meaning

The bracket records the action of Hamiltonian dynamics on observables:
\[
\{f,g\}=X_g(f)
\]
under the convention \(\iota_{X_g}\omega=dg\). Therefore \(\{f,H\}\) is the rate of change of \(f\) along the [[differential-geometry/hamiltonian-flow|Hamiltonian flow]] of \(H\). On a connected symplectic manifold, the Poisson center consists exactly of the constant functions.

## Maps and examples

The canonical bracket on \(\mathbb R^{2n}\) satisfies \(\{q^i,p_j\}=\delta^i_j\). A [[differential-geometry/symplectomorphism|symplectomorphism]] induces an isomorphism of Poisson algebras by pullback. More generally, a [[differential-geometry/poisson-map|Poisson map]] is precisely a [[fiber-bundles/smooth-map|smooth map]] whose pullback preserves brackets.

For a general [[differential-geometry/poisson-manifold|Poisson manifold]], the same axioms define a Poisson algebra on smooth functions, but its Poisson center may contain nonconstant Casimir functions.

## Conventions and scope

The real-valued algebra is used here. One may instead complexify to \(C^\infty(M,\mathbb C)\) and extend the bracket complex-bilinearly. The phrase “classical [[stat-mech-quantum/observable-algebra|observable algebra]]” often refers to a chosen subalgebra of admissible observables rather than all smooth functions, especially in systems with constraints or analytic restrictions.

## References

1. Jerrold E. Marsden and Tudor S. Ratiu, *Introduction to Mechanics and Symmetry*, 2nd ed., Springer, 1999. [DOI record](https://doi.org/10.1007/978-0-387-21792-5). Relevant: §10.1, Poisson brackets and Hamiltonian dynamics.
2. Izu Vaisman, *Lectures on the Geometry of Poisson Manifolds*, Birkhäuser, 1994. [DOI record](https://doi.org/10.1007/978-3-0348-8495-2). Relevant: Chapter 1, Poisson algebras and Poisson manifolds.
