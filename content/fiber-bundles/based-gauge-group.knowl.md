+++
id = "fiber-bundles/based-gauge-group"
title = "Based gauge group"
kind = "definition"
summary = "The subgroup of gauge transformations that fixes a chosen point in a principal-bundle fiber."
aliases = ["pointed gauge group", "framed gauge group"]
domains = ["fiber-bundles", "differential-geometry"]
section_mode = "progressive"
+++

Let \(\pi:P\to M\) be a [[fiber-bundles/principal-g-bundle|principal bundle]], choose \(x_0\in M\), and choose any point \(p_0\in P_{x_0}\). The **based gauge group** is the subgroup
\[
\mathcal G_{p_0}(P)=\{\Phi\in\mathcal G(P):\Phi(p_0)=p_0\}
\]
of the [[fiber-bundles/gauge-group|gauge group]] \(\mathcal G(P)\). Equivalently, if a [[fiber-bundles/gauge-transformation|gauge transformation]] is represented by an [[fiber-bundles/equivariant-map|equivariant map]] \(u:P\to G\) through \(\Phi_u(p)=p\,u(p)\), then \(\Phi_u\) is based exactly when \(u(p_0)=e\). Equivariance then gives \(u(p_0g)=g^{-1}u(p_0)g=e\), so \(\Phi_u\) fixes every point of the fiber \(P_{x_0}\).

## Dependence on the framing

Replacing \(p_0\) by \(p_0g\) conjugates the evaluation map to \(G\) by \(g\), but conjugation fixes the identity. Its kernel, and hence the based subgroup, is therefore literally independent of the choice of \(p_0\) in the fiber. One may consequently write \(\mathcal G_{x_0}(P)\). A framing or trivialization at \(x_0\) is needed only to identify the evaluation map with a particular copy of \(G\); under such an identification, the based condition is the familiar requirement that a gauge function \(u:M\to G\) satisfy \(u(x_0)=e\).

## Action on connections

The based group acts by pullback on the space of [[fiber-bundles/principal-connection|principal connections]]. If \(M\) is connected, a gauge transformation preserving a connection is determined by its value at one point through parallel transport. Consequently, its stabilizer inside \(\mathcal G_{p_0}(P)\) is trivial. This is why based gauge groups are used to form free gauge quotients.

## Conventions and scope

**Warning.** “Framed gauge group” more generally means transformations equal to the identity along specified framing data, which may lie on a boundary, an end, or a submanifold rather than at one point. In this knowl it is an alias only for transformations restricting to the identity on the fiber over the chosen base point.

## References

1. Daniel S. Freed and Karen K. Uhlenbeck, *Instantons and Four-Manifolds*, 2nd ed., Springer, 1991. [DOI record](https://doi.org/10.1007/978-1-4613-9703-8). Relevant: Chapter 3, based gauge transformations and free gauge actions.
2. Mark J. D. Hamilton, *Mathematical Gauge Theory*, Springer, 2017. [DOI record](https://doi.org/10.1007/978-3-319-68439-0). Relevant: gauge groups, their action on connections, and stabilizers.
