+++
id = "differential-geometry/poisson-map"
title = "Poisson map"
kind = "definition"
summary = "A Poisson map is a smooth map whose pullback preserves Poisson brackets."
aliases = ["Poisson morphism"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \((M,\{-,-\}_M)\) and \((N,\{-,-\}_N)\) be [[differential-geometry/poisson-manifold|Poisson manifolds]]. A [[fiber-bundles/smooth-map|smooth map]] \(\Phi:M\to N\) is a **Poisson map** if
\[
\{f,g\}_N\circ\Phi=\{f\circ\Phi,g\circ\Phi\}_M
\]
for all \(f,g\in C^\infty(N)\). Thus the pullback homomorphism \(\Phi^*:C^\infty(N)\to C^\infty(M)\) is also a homomorphism of Poisson algebras. If \(\pi_M\) and \(\pi_N\) are the corresponding Poisson bivectors, the same condition is
\[
(\wedge^2d\Phi_p)\pi_M(p)=\pi_N(\Phi(p))
\]
for every \(p\in M\).
This condition is contravariant because functions pull back from the target
to the source.

## Equivalent viewpoints

The bracket and bivector tests are equivalent because the differential of a pullback satisfies \(d(f\circ\Phi)_p=d\Phi_p^*(df_{\Phi(p)})\). The equality need only be checked locally on coordinate functions and their smooth combinations.

When both Poisson structures are nondegenerate and arise from symplectic forms, a diffeomorphism is Poisson exactly when it is a [[differential-geometry/symplectomorphism|symplectomorphism]], with the compatible sign convention relating the forms and bivectors.

## Structure and consequences

Identity maps are Poisson, and the composite of Poisson maps is Poisson. Hence Poisson manifolds and Poisson maps form a category. A Poisson map sends Hamiltonian dynamics contravariantly: the pullback of a Hamiltonian on \(N\) has a [[differential-geometry/hamiltonian-vector-field|Hamiltonian vector field]] that is \(\Phi\)-related to the original one whenever the displayed tensor identity applies.

More explicitly, \(d\Phi(X_{f\circ\Phi}^M)=X_f^N\circ\Phi\) for every \(f\in C^\infty(N)\). Poisson diffeomorphisms preserve the rank of the Poisson tensor and therefore carry symplectic leaves to symplectic leaves.

## Examples and non-examples

The projection \(M\times N\to M\) is Poisson for the product Poisson structure. A constant map with value \(q\in N\) is Poisson exactly when \(\pi_N(q)=0\).

A constant map into a positive-dimensional [[differential-geometry/symplectic-manifold|symplectic manifold]] is therefore not Poisson: its differential pushes every bivector to zero, whereas the target Poisson bivector is nonzero. This failure shows that not every smooth map between Poisson manifolds is a Poisson map.

## Conventions and scope

**Warning.** Replacing one Poisson bracket by its negative changes which maps are Poisson versus anti-Poisson. The definition here is covariant at the manifold level and contravariant on functions. In algebraic geometry and singular settings, “Poisson morphism” is expressed directly as preservation of brackets on structure sheaves; this knowl uses smooth finite-dimensional manifolds.

## References

1. Izu Vaisman, *Lectures on the Geometry of Poisson Manifolds*, Progress in Mathematics 118, Birkhäuser, 1994. [Publisher record](https://doi.org/10.1007/978-3-0348-8495-2). Relevant: “Poisson Morphisms, Coinduced Structures, Reduction,” pp. 97–114.
2. Jerrold E. Marsden and Tudor S. Ratiu, *Introduction to Mechanics and Symmetry*, 2nd ed., Texts in Applied Mathematics 17, Springer, 1999. [Publisher record](https://doi.org/10.1007/978-0-387-21792-5). Relevant: Chapter 10, “Poisson Manifolds.”
