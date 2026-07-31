+++
id = "algebra-topological/ideal-of-definition"
title = "Ideal of definition"
kind = "definition"
summary = "An ideal whose powers form a neighborhood basis of zero in a linearly topologized ring."
aliases = ["adic ideal of definition", "defining ideal of an adic ring"]
domains = ["algebra-topological", "algebraic-geometry-foundations"]
section_mode = "progressive"
+++

Let \(A\) be a commutative topological ring. An open ideal \(I\subseteq A\)
is an **ideal of definition** if
\[
I,\ I^2,\ I^3,\ldots
\]
is a neighborhood basis of \(0\). Equivalently, the given topology on \(A\)
is the \(I\)-adic topology.

In the classical adic convention used for formal schemes, an ideal of
definition is required to be finitely generated. A topological ring that has
such an ideal is an [[algebra-topological/adic-ring|adic ring]].

## Choice of ideal

An ideal of definition is not generally unique. If \(I\) and \(J\) are ideals
of definition for the same topology, their powers are cofinal: for every
\(m\) there is an \(n\) with \(I^n\subseteq J^m\), and conversely. Thus the
topology and its completion do not depend on which ideal of definition is
chosen.

For the discrete topology, \(0\) is an ideal of definition. A nonzero
nilpotent ideal can also define the discrete topology.

## Reference

The Stacks Project Authors, “Topological rings and modules.”
[Section 15.36, Tag 07E8](https://stacks.math.columbia.edu/tag/07E8).
