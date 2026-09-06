+++
id = "fiber-bundles/moduli-space-of-flat-connections"
title = "Moduli space of flat connections"
kind = "definition"
summary = "The quotient of the space of flat connections on a fixed principal bundle by gauge equivalence."
aliases = ["flat-connection moduli", "flat gauge moduli"]
domains = ["fiber-bundles", "differential-geometry"]
prerequisites = ["fiber-bundles/principal-g-bundle", "fiber-bundles/gauge-group", "fiber-bundles/curvature-2-form-of-a-principal-connection", "fiber-bundles/gauge-transformation", "fiber-bundles/flat-principal-connection"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(P\to M\) be a smooth [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]]. Write \(\mathcal A(P)\) for its space of connections and \(\mathcal G(P)\) for its [[fiber-bundles/gauge-group|gauge group]]. The **moduli space of flat connections on \(P\)** is
\[
\mathcal M_{\mathrm{flat}}(P)
=
\{A\in\mathcal A(P):F_A=0\}\big/\mathcal G(P),
\]
where \(F_A\) is the [[fiber-bundles/curvature-2-form-of-a-principal-connection|curvature]] and the quotient identifies connections related by a [[fiber-bundles/gauge-transformation|gauge transformation]]. Unless a topology, differentiable structure, or stack is specified, this notation denotes only the set of gauge-equivalence classes of [[fiber-bundles/flat-principal-connection|flat connections]] on the fixed underlying bundle \(P\).

## Local structure

At a flat connection \(A\), the [[fiber-bundles/deformation-complex-of-a-flat-connection|twisted de Rham complex]] describes the infinitesimal quotient. Its zeroth cohomology is the [[lie-groups/lie-algebra|Lie algebra]] of the stabilizer, its first cohomology gives infinitesimal deformations modulo infinitesimal gauge, and its second cohomology contains obstruction classes. Consequently, the quotient is generally singular at connections with extra stabilizer or obstructed deformations; it should not be assumed to be a manifold.

Analytic constructions normally complete connections and gauge transformations in compatible Sobolev norms and use a slice for the gauge action. On compact bases the resulting finite-dimensional local models recover the same smooth flat connections after elliptic regularity.

## Relation to representations

If \(M\) is connected, choosing a basepoint and a point of the fiber assigns to \(A\) its [[fiber-bundles/holonomy-representation|holonomy representation]] \(\pi_1(M)\to G\). Changing the chosen fiber point conjugates the representation. The [[fiber-bundles/holonomy-correspondence-for-flat-connections|holonomy correspondence]] therefore identifies isomorphism classes of flat bundles with [[algebra-groups/conjugacy-class|conjugacy classes]] of representations. Restricting to a fixed \(P\) selects only those representations whose associated flat bundle has the topological type of \(P\).

For a closed oriented surface, the smooth irreducible locus inherits a symplectic form from the [[fiber-bundles/atiyah-bott-symplectic-form|Atiyah–Bott form]].

## Example

For the trivial \(U(1)\)-bundle over a closed connected manifold,
\[
\mathcal M_{\mathrm{flat}}\cong
H^1(M;\mathbb R)\big/2\pi H^1(M;\mathbb Z).
\]
For a genus-\(g\) closed surface this is a \(2g\)-dimensional torus. Nonabelian examples can have several components and singular strata.

## References

1. Michael F. Atiyah and Raoul Bott, “The Yang–Mills Equations over Riemann Surfaces,” *Philosophical Transactions of the Royal Society of London A* 308 (1983), 523–615. [DOI record](https://doi.org/10.1098/rsta.1983.0017). Relevant: §§6 and 9, flat connections and symplectic reduction.
2. William M. Goldman, “The Symplectic Nature of Fundamental Groups of Surfaces,” *Advances in Mathematics* 54 (1984), 200–225. [DOI record](https://doi.org/10.1016/0001-8708%2884%2990040-9). Relevant: §§1–2, representation moduli and their symplectic structure.
