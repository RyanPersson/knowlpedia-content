+++
id = "differential-geometry/hamiltonian-torus-action"
title = "Hamiltonian torus action"
kind = "definition"
summary = "A Hamiltonian torus action is a symplectic action of a compact torus equipped with a torus-invariant moment map."
aliases = ["symplectic torus action with moment map"]
domains = ["differential-geometry", "lie-groups"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "differential-geometry/symplectic-manifold", "differential-geometry/hamiltonian-lie-group-action", "fiber-bundles/moment-map", "differential-geometry/hamiltonian-function", "differential-geometry/hamiltonian-vector-field", "algebra-groups/group-action"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(T\) be a compact torus with [[lie-groups/lie-algebra|Lie algebra]] \(\mathfrak t\), acting on a [[differential-geometry/symplectic-manifold|symplectic manifold]] \((M,\omega)\). A **Hamiltonian torus action** is a [[differential-geometry/hamiltonian-lie-group-action|Hamiltonian Lie group action]] with a map \(\mu:M\to\mathfrak t^*\) satisfying
\[
d\langle\mu,\xi\rangle=\iota_{\xi_M}\omega
\]
for every \(\xi\in\mathfrak t\), and \(\mu(tx)=\mu(x)\) for \(t\in T\). The second condition is equivariance: because \(T\) is abelian, its coadjoint action on \(\mathfrak t^*\) is trivial. The integral lattice \(\ker(\exp:\mathfrak t\to T)\) records which infinitesimal generators integrate to periodic circle actions.

## Components and normalization

Each \(\xi\in\mathfrak t\) determines a [[differential-geometry/hamiltonian-function|Hamiltonian function]]
\[
\mu^\xi=\langle\mu,\xi\rangle
\]
whose [[differential-geometry/hamiltonian-vector-field|Hamiltonian vector field]] is the infinitesimal generator \(\xi_M\). The [[fiber-bundles/moment-map|moment map]] is determined only up to addition of a constant element of \(\mathfrak t^*\). Translating \(\mu\) changes neither the action nor its component [[fiber-bundles/vector-field|vector fields]].

Lattice conventions vary: some authors define \(T=\mathfrak t/\Lambda\), while others take the exponential kernel to be \(2\pi\Lambda\). Statements involving integral weights or polytope labels must retain the chosen convention.

## Convexity and toric actions

If \(M\) is compact and connected, the [[differential-geometry/atiyah-guillemin-sternberg-convexity-theorem|Atiyah–Guillemin–Sternberg convexity theorem]] says that \(\mu(M)\) is the [[convex-analysis/convex-hull|convex hull]] of the images of the \(T\)-fixed-point components; in particular it is a convex polytope. This special convexity is one reason torus actions are more rigid than general Hamiltonian [[algebra-groups/group-action|group actions]].

When the action is effective and \(\dim T=\frac12\dim M\), the Hamiltonian \(T\)-space is called symplectic toric. Compact connected symplectic toric manifolds are classified, up to the appropriate equivariant [[differential-geometry/symplectomorphism|symplectomorphism]], by Delzant polytopes.

## Standard example

The coordinatewise action of \(T^n\) on \(\mathbb C^n\),
\[
(e^{it_1},\ldots,e^{it_n})\cdot(z_1,\ldots,z_n)
=(e^{it_1}z_1,\ldots,e^{it_n}z_n),
\]
is Hamiltonian. For \(\omega=\sum_j dx_j\wedge dy_j\) and the sign convention in the core, one moment map is
\[
\mu(z)=-\frac12\bigl(|z_1|^2,\ldots,|z_n|^2\bigr).
\]
Changing the convention for Hamiltonian vector fields reverses this sign.

## References

1. Victor Guillemin, *Moment Maps and Combinatorial Invariants of Hamiltonian \(T^n\)-Spaces*, Birkhäuser, 1994. [DOI record](https://doi.org/10.1007/978-1-4612-0269-1). Relevant: chapter 1, Hamiltonian torus actions, moment polytopes, and Delzant spaces.
2. Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Springer, 2008. [DOI record](https://doi.org/10.1007/978-3-540-45330-7). Relevant: chapters on moment maps, symplectic reduction, and symplectic toric manifolds.
