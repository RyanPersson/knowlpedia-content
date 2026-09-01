+++
id = "algebraic-geometry-foundations/generic-point"
title = "Generic point"
kind = "definition"
summary = "A point whose closure is an entire irreducible closed subset."
aliases = ["generic point", "generic point of an irreducible subset"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/scheme", "topology/irreducible-space"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
+++

Let \(X\) be a [[algebraic-geometry-foundations/scheme|scheme]] and \(Z\subseteq X\) an [[topology/irreducible-space|irreducible closed subset]]. A point \(\eta\in Z\) is a **generic point of \(Z\)** if
\[
\overline{\{\eta\}}=Z.
\]

Every irreducible closed subset of a scheme has a unique generic point.

## Example

If \(A\) is an [[algebra-rings/integral-domain|integral domain]], the [[algebra-rings/prime-ideal|prime ideal]] \((0)\) is the generic point of \(\operatorname{Spec}A\), because its closure is the entire [[algebra-commutative/prime-spectrum|prime spectrum]]. Thus the point \((0)\) in \(\operatorname{Spec}k[x]\) records properties holding away from every proper algebraic condition; it is not a missing numerical value of \(x\).

## Remark

A generic point is an actual point of the Zariski topological space, not a probabilistically typical point or a metric limit point. It need not be closed.
