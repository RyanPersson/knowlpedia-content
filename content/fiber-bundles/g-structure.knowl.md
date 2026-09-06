+++
id = "fiber-bundles/g-structure"
title = "G-structure"
kind = "definition"
summary = "A reduction of the frame bundle of a smooth manifold to a specified Lie subgroup of the general linear group."
aliases = ["G-structure on a manifold", "reduction of the frame bundle"]
domains = ["fiber-bundles", "differential-geometry"]
prerequisites = ["lie-groups/lie-subgroup", "fiber-bundles/reduction-of-structure-group", "fiber-bundles/frame-bundle-fr-of-a-manifold-m"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(M\) be a smooth \(n\)-manifold and let \(G\subseteq\mathrm{GL}(n,\mathbb R)\) be a [[lie-groups/lie-subgroup|Lie subgroup]]. A **\(G\)-structure** on \(M\) is a [[fiber-bundles/reduction-of-structure-group|reduction of structure group]] of the [[fiber-bundles/frame-bundle-fr-of-a-manifold-m|frame bundle]] \(\mathrm{Fr}(TM)\) from \(\mathrm{GL}(n,\mathbb R)\) to \(G\). Concretely, it is a principal \(G\)-subbundle \(Q\subseteq\mathrm{Fr}(TM)\) whose fiber \(Q_x\) consists of the frames at \(x\) declared compatible with the structure. The fixed inclusion \(G\hookrightarrow\mathrm{GL}(n,\mathbb R)\) is part of the ambient data and determines how \(G\) changes those frames.

## Geometric examples

An orientation is a \(\mathrm{GL}^+(n,\mathbb R)\)-structure, and a Riemannian metric is equivalently an \(\mathrm O(n)\)-structure. On a \(2m\)-manifold, an almost complex structure gives a \(\mathrm{GL}(m,\mathbb C)\)-structure, while a fiberwise nondegenerate alternating form gives an \(\mathrm{Sp}(2m,\mathbb R)\)-structure.

## Integrability and connections

A \(G\)-structure is pointwise reduction data; it need not be locally equivalent to the flat model. Integrability imposes additional differential conditions that depend on \(G\). Likewise, a connection on \(\mathrm{Fr}(TM)\) need not preserve \(Q\); preservation is the separate condition of being a [[fiber-bundles/connection-compatible-with-a-reduction|connection compatible with the reduction]].

For example, an \(\mathrm{Sp}(2m,\mathbb R)\)-structure supplies a nondegenerate two-form, but it defines a [[differential-geometry/symplectic-manifold|symplectic manifold]] only when that form is also closed.

## Conventions and scope

**Warning.** This is the classical first-order definition with a specified subgroup \(G\subseteq\mathrm{GL}(n,\mathbb R)\). Some treatments permit a homomorphism \(G\to\mathrm{GL}(n,\mathbb R)\), higher-order frame bundles, or generalized \(G\)-structures. Those broader notions require extra data and are not included here.

## References

1. Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, Volume I, Wiley Classics, 1996. [Publisher record](https://www.wiley-vch.de/en/areas-interest/mathematics-statistics/mathematics-16ma/geometry-topology-16ma6/foundations-of-differential-geometry-volume-1-978-0-471-15733-5). Relevant: Chapter I, frame bundles, reductions, and \(G\)-structures.
2. Shlomo Sternberg, *Lectures on Differential Geometry*, 2nd ed., Chelsea, 1983. [AMS record](https://bookstore.ams.org/chel-316). Relevant: Chapter VII, \(G\)-structures and equivalence problems.
