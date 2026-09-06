+++
id = "differential-geometry/symplectic-lie-group-action"
title = "Symplectic Lie group action"
kind = "definition"
summary = "A smooth Lie group action whose transformations preserve the symplectic form."
aliases = ["symplectic action"]
domains = ["differential-geometry", "lie-groups"]
section_mode = "progressive"
prerequisites = ["fiber-bundles/lie-group", "differential-geometry/symplectic-manifold", "fiber-bundles/smooth-action-of-a-lie-group-on-a-manifold", "differential-geometry/symplectomorphism"]
dependency_heuristic = "semantic-spotcheck-review-v1"
dependency_review_count = 2
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] and let \((M,\omega)\) be
a [[differential-geometry/symplectic-manifold|symplectic manifold]]. A
[[fiber-bundles/smooth-action-of-a-lie-group-on-a-manifold|smooth action]]
\(\Phi:G\times M\to M\) is a **symplectic Lie group action** if, for every
\(g\in G\), the diffeomorphism \(\Phi_g(x)=\Phi(g,x)\) is a
[[differential-geometry/symplectomorphism|symplectomorphism]]:
\[
\Phi_g^*\omega=\omega.
\]
Equivalently, the action homomorphism sends \(G\) into the group of
symplectomorphisms of \((M,\omega)\). The definition requires preservation of
the specified symplectic form, not merely of its cohomology class or of the
associated volume form.

## Infinitesimal criterion

For \(\xi\) in the [[lie-groups/lie-algebra|Lie algebra]] of \(G\), let
\(\xi_M\) be the corresponding
infinitesimal generator. A symplectic action satisfies
\[
\mathcal L_{\xi_M}\omega=0.
\]
Since \(d\omega=0\), Cartan's formula makes this equivalent to
\(d(\iota_{\xi_M}\omega)=0\). Conversely, this infinitesimal condition implies
that the identity component of \(G\) acts symplectically. If \(G\) is
disconnected, its other components must still be checked separately.

## Relationship to Hamiltonian actions

A [[differential-geometry/hamiltonian-lie-group-action|Hamiltonian action]] is a symplectic action supplied with a
[[fiber-bundles/moment-map|moment map]] whose components have
[[differential-geometry/hamiltonian-vector-field|Hamiltonian vector fields]]
equal, up to the adopted sign convention, to the infinitesimal generators.
Symplecticity alone only says
that the \(1\)-forms \(\iota_{\xi_M}\omega\) are closed; Hamiltonianity requires
them to be exact in a compatible and usually equivariant way. Thus a
symplectic action need not be Hamiltonian when first cohomology provides an
obstruction.

## Examples and non-examples

The standard rotation action of \(SO(2)\) on
\((\mathbb R^2,dx\wedge dy)\) is symplectic and Hamiltonian. Translation of
the symplectic torus by the torus itself is symplectic, but its generating
constant \(1\)-forms need not be exact, so the action is not Hamiltonian.
A diffeomorphism preserving only \(\omega^n\) is volume-preserving but need
not be symplectic when \(\dim M\geq4\).

## References

1. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: Chapter 5 on symplectic and Hamiltonian group actions.
2. Juan-Pablo Ortega and Tudor S. Ratiu, *Momentum Maps and Hamiltonian Reduction*, Birkhäuser, 2004. [DOI record](https://doi.org/10.1007/978-1-4757-3811-7). Relevant: the chapters on Lie group actions and the standard momentum map.
