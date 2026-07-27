+++
id = "differential-geometry/comoment-map"
title = "Comoment map"
kind = "definition"
summary = "A Lie algebra homomorphism assigning to each infinitesimal symmetry its Hamiltonian function."
aliases = ["co-moment map"]
domains = ["differential-geometry", "lie-groups"]
section_mode = "progressive"
+++

Let \(G\) act on \((M,\omega)\) by a [[differential-geometry/symplectic-lie-group-action|symplectic action]], with [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak g\), and use \(\iota_{X_f}\omega=df\). A **comoment map** is a [[linear-algebra/linear-map|linear map]]
\[
c:\mathfrak g\longrightarrow C^\infty(M),\qquad \xi\longmapsto c(\xi),
\]
such that \(dc(\xi)=\iota_{\xi_M}\omega\) and
\[
c([\xi,\eta])=\{c(\xi),c(\eta)\}
\]
for all \(\xi,\eta\in\mathfrak g\). Thus \(c\) is a [[lie-groups/lie-algebra-homomorphism|Lie algebra homomorphism]] into the [[differential-geometry/poisson-algebra-smooth-functions|Poisson algebra of smooth functions]], and each \(c(\xi)\) generates the [[differential-geometry/infinitesimal-generator-lie-action|infinitesimal action]] associated with \(\xi\). The differential axiom identifies the generating [[fiber-bundles/vector-field|vector fields]]; the bracket axiom requires the chosen Hamiltonians to respect the Lie algebra exactly, rather than only up to constants.

## Relationship to moment maps

A [[fiber-bundles/moment-map|moment map]] \(\mu:M\to\mathfrak g^*\) determines the linear assignment
\[
c_\mu(\xi)=\mu^\xi=\langle\mu,\xi\rangle.
\]
The differential condition for \(c_\mu\) is exactly the componentwise moment-map identity. Under the conventions in the core, the bracket condition is infinitesimal equivariance of \(\mu\); for connected \(G\), it is equivalent to global coadjoint equivariance [Ortega and Ratiu, §4.2](https://doi.org/10.1007/978-1-4757-3811-7).

Conversely, a comoment map defines \(\mu\) uniquely by \(\langle\mu(x),\xi\rangle=c(\xi)(x)\), because \(c\) is linear in \(\xi\).

## Obstruction to bracket preservation

If a linear choice of Hamiltonians satisfies only the differential condition, then
\[
\sigma(\xi,\eta)
=\{c(\xi),c(\eta)\}-c([\xi,\eta])
\]
is locally constant on \(M\). On a connected manifold it is a real-valued Lie-algebra \(2\)-cocycle. Changing \(c\) by constants changes \(\sigma\) by a coboundary, so the resulting cohomology class measures the obstruction to converting the weak assignment into a comoment map.

## Conventions and scope

**Warning.** Some sources use “comoment map” for the linear transpose of any moment map before bracket preservation is imposed. In that usage, the second displayed axiom characterizes an equivariant comoment map. A quantum moment map is a deformation-theoretic analogue into a noncommutative algebra, not a lexical synonym for the classical notion defined here.

## References

1. Victor Guillemin and Shlomo Sternberg, *Symplectic Techniques in Physics*, Cambridge University Press, 1984. [DOI record](https://doi.org/10.1017/CBO9780511624110). Relevant: Chapter 3, infinitesimal Hamiltonians and moment maps.
2. Juan-Pablo Ortega and Tudor S. Ratiu, *Momentum Maps and Hamiltonian Reduction*, Birkhäuser, 2004. [DOI record](https://doi.org/10.1007/978-1-4757-3811-7). Relevant: §4.2, infinitesimal equivariance and the cocycle obstruction.
