+++
id = "algebraic-geometry-foundations/closed-point"
title = "Closed point"
kind = "definition"
summary = "A point whose singleton is closed in the underlying topological space of a scheme."
aliases = ["closed point", "closed scheme point"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/scheme", "algebraic-geometry-foundations/affine-scheme", "algebra-rings/prime-ideal", "algebra-rings/maximal-ideal"]
dependency_review_count = 1
+++

A point \(x\) of a [[algebraic-geometry-foundations/scheme|scheme]] \(X\) is a **closed point** if its singleton is closed:

\[
\overline{\{x\}}=\{x\}.
\]

For an [[algebraic-geometry-foundations/affine-scheme|affine scheme]] \(X=\operatorname{Spec}A\), the point corresponding to a [[algebra-rings/prime-ideal|prime ideal]] \(\mathfrak p\) is closed if and only if \(\mathfrak p\) is maximal. Thus the closed points of \(\operatorname{Spec}A\) are precisely the [[algebra-rings/maximal-ideal|maximal ideals]] of \(A\).

## Examples

For \(\operatorname{Spec}F\) with \(F\) a field, the unique point is closed. In \(\operatorname{Spec}k[x]\), the points \((x-a)\) for \(a\in k\) are the familiar geometric points when \(k\) is algebraically closed, while \((0)\) is the [[algebraic-geometry-foundations/generic-point|generic point]] and is not closed.

## Remarks

If \(X\) is of finite type over an [[algebraic-geometry-foundations/algebraically-closed-field|algebraically closed field]] \(k\), its closed points have [[algebra-commutative/residue-field|residue field]] \(k\) and correspond to the classical geometric points described by coordinates.

**Warning.** Not every point of a scheme is closed. This differs from Hausdorff spaces and manifolds, where all singleton subsets are closed.
