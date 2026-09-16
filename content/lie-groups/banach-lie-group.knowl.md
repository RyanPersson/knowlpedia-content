+++
id = "lie-groups/banach-lie-group"
title = "Banach–Lie group"
kind = "definition"
summary = "A group with a smooth Banach-manifold structure for which multiplication and inversion are smooth."
aliases = ["Banach Lie group"]
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["algebra-groups/group", "differential-geometry/banach-manifold"]
+++

A **Banach–Lie group** is a [[algebra-groups/group|group]] \(G\) equipped with a [[differential-geometry/banach-manifold|smooth Banach-manifold]] structure such that
\[
m:G\times G\longrightarrow G,\quad m(g,h)=gh,
\qquad
\operatorname{inv}:G\longrightarrow G,\quad g\longmapsto g^{-1}
\]
are smooth. Its model space may be infinite-dimensional.

## Tangent Lie algebra

The tangent space \(\mathfrak g=T_eG\) is a Banach space. The bracket obtained from left-invariant vector fields is continuous and bilinear, and the exponential map is a local diffeomorphism near \(0\). Finite-dimensional Lie groups are special cases.

## Example and scope

The additive group of a Banach space is a Banach–Lie group. The [[lie-groups/norm-unitary-group|unitary group with operator-norm topology]] is another example.

A group with a weaker topology does not inherit this smooth structure merely because it has the same underlying elements. In particular, strong continuity of a unitary representation need not make it a smooth map into the norm-topology unitary group.

## References

1. Karl-Hermann Neeb, [*On Differentiable Vectors for Representations of Infinite Dimensional Lie Groups*](https://arxiv.org/abs/1002.1602). §2, definition of locally convex Lie groups and the Banach–Lie specialization.
