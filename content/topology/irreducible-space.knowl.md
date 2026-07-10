+++
id = "topology/irreducible-space"
title = "Irreducible space"
kind = "definition"
summary = "A nonempty topological space that is not the union of two proper closed subsets."
aliases = ["irreducible space", "irreducible topological space", "irreducible subset"]
domains = ["topology"]
+++

A nonempty [[topology/topological-space|topological space]] \(X\) is **irreducible** if it cannot be written as the union of two proper [[topology/closed-set|closed subsets]]. Equivalently, every two nonempty open subsets of \(X\) intersect.

A subset \(Z\subseteq X\) is irreducible if it is irreducible with its [[topology/subspace-topology|subspace topology]]. An **irreducible component** of \(X\) is a maximal irreducible subset; every irreducible component is closed.

If a point \(\eta\in X\) has [[topology/closure|closure]] equal to \(X\), then \(X\) is irreducible and \(\eta\) is its [[algebraic-geometry-foundations/generic-point|generic point]]. In particular, if \(A\) is an [[algebra-rings/integral-domain|integral domain]], then the [[algebra-commutative/prime-spectrum|prime spectrum]] \(\operatorname{Spec}A\) is irreducible, with generic point \((0)\).

**Warning.** Irreducible is stronger than [[topology/connected-set|connected]]: an irreducible space is connected, but a connected space need not be irreducible.
