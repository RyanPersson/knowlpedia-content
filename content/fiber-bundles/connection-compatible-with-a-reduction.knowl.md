+++
id = "fiber-bundles/connection-compatible-with-a-reduction"
title = "Connection compatible with a reduction"
kind = "definition"
summary = "A principal connection whose horizontal spaces restrict to a chosen reduction of the structure group."
aliases = ["connection preserving an H-reduction", "adapted connection", "reduction-compatible connection"]
domains = ["fiber-bundles", "differential-geometry"]
prerequisites = ["lie-groups/lie-subgroup", "fiber-bundles/reduction-of-structure-group", "fiber-bundles/principal-g-bundle", "fiber-bundles/principal-connection"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(H\subseteq G\) be a [[lie-groups/lie-subgroup|Lie subgroup]], let \(i:Q\hookrightarrow P\) be a [[fiber-bundles/reduction-of-structure-group|reduction of structure group]] of a [[fiber-bundles/principal-g-bundle|principal \(G\)-bundle]], and let \(A\) be a [[fiber-bundles/principal-connection|principal connection]] on \(P\). The connection \(A\) is **compatible with the reduction** \(Q\) when its horizontal subspace at every \(q\in Q\) lies in \(T_qQ\). Equivalently, the restricted connection form \(i^*A\) takes values in the Lie algebra \(\mathfrak h\subseteq\mathfrak g\); then \(i^*A\), regarded as an \(\mathfrak h\)-valued form, is a principal \(H\)-connection on \(Q\).

## Restriction and extension

A compatible \(G\)-connection restricts uniquely to an \(H\)-connection on \(Q\). Conversely, every principal \(H\)-connection on \(Q\) extends uniquely to a principal \(G\)-connection on the extended bundle \(Q\times_HG\), hence on \(P\) after choosing the reduction isomorphism. This correspondence is the connection-level counterpart of [[fiber-bundles/extension-of-structure-group|extension of structure group]].

## Parallel transport and holonomy

Compatibility means that horizontal lifts beginning in \(Q\) remain in \(Q\). Therefore parallel transport preserves the reduced subbundle, and the [[fiber-bundles/holonomy-group|holonomy group]] computed from a point \(q\in Q\) lies in \(H\). Conversely, the [[fiber-bundles/holonomy-reduction-principle|holonomy reduction principle]] constructs a preserved reduction from suitable holonomy containment, subject to its connectedness and reduction hypotheses.

## Conventions and scope

**Warning.** The phrase “the restriction of \(A\) to \(Q\)” is meaningful as a principal \(H\)-connection only after verifying that \(i^*A\) is \(\mathfrak h\)-valued. An arbitrary \(G\)-connection need not preserve a fixed reduction. This knowl uses [[fiber-bundles/right-principal-action|right principal actions]] and the corresponding standard equivariance convention for connection forms.

## References

1. Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, Volume I, Wiley Classics, 1996. [Publisher record](https://www.wiley-vch.de/en/areas-interest/mathematics-statistics/mathematics-16ma/geometry-topology-16ma6/foundations-of-differential-geometry-volume-1-978-0-471-15733-5). Relevant: Chapter II, connections on reductions and extension of structure group.
2. Arthur L. Besse, *Einstein Manifolds*, Springer, 1987. [DOI record](https://doi.org/10.1007/978-3-540-74311-8). Relevant: Chapter 10, holonomy reductions and preserved geometric structures.
