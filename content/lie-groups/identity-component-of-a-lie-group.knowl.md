+++
id = "lie-groups/identity-component-of-a-lie-group"
title = "Identity component of a Lie group"
kind = "definition"
summary = "The connected component containing the identity; it is an open normal Lie subgroup with discrete quotient."
aliases = ["identity component", "neutral component", "connected component of the identity", "G zero"]
domains = ["lie-groups", "topology"]
prerequisites = ["fiber-bundles/lie-group", "topology/connected-component", "lie-groups/normal-lie-subgroup"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(G\) be a [[fiber-bundles/lie-group|Lie group]] with identity \(e\). The
**identity component** (or **neutral component**) of \(G\) is the
[[topology/connected-component|connected component]]

\[
G^{\circ}=G_e
\]

that contains \(e\). It is a connected, open-and-closed
[[lie-groups/normal-lie-subgroup|normal Lie subgroup]] of \(G\), and every
connected component of \(G\) is a left and right coset of \(G^{\circ}\).

## Component group and Lie algebra

The quotient

\[
\pi_0(G)=G/G^{\circ}
\]

is a discrete group, called the **component group** of \(G\). It records the
global disconnectedness that is invisible to infinitesimal Lie theory.
Indeed, the inclusion \(G^{\circ}\hookrightarrow G\) induces an isomorphism

\[
\operatorname{Lie}(G^{\circ})\cong\operatorname{Lie}(G).
\]

Thus a [[lie-groups/lie-algebra|Lie algebra]] determines the local group structure but does not determine
the component group.

## Why it is normal and open

Conjugation by any \(g\in G\) is a homeomorphism fixing \(e\), so it preserves
the component containing \(e\); hence \(gG^{\circ}g^{-1}=G^{\circ}\). A
finite-dimensional manifold is locally connected, so its connected components
are open. The other components are then the translates \(gG^{\circ}\).

## Stabilizer warning

If a possibly disconnected Lie group acts on a space and \(G_x\) is a
[[lie-groups/stabilizer-lie-group|stabilizer]], three groups can differ:

\[
(G_x)^{\circ},\qquad G_x\cap G^{\circ},\qquad G_x.
\]

The first is the identity component of the stabilizer, the second is the full
stabilizer inside the acting identity component, and the third may contain
additional components. Neither of the first two should be substituted for the
full stabilizer without checking connectedness. This distinction matters in
homogeneous-space descriptions of real Grassmannians and frame spaces.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2013,
   Chapter 20. [Publisher record](https://doi.org/10.1007/978-1-4419-9982-5).
2. J. J. Duistermaat and J. A. C. Kolk, *Lie Groups*, Springer, 2000,
   Chapter 1. [Publisher record](https://doi.org/10.1007/978-3-642-56936-4).
