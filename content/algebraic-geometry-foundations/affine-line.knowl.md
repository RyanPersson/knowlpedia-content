+++
id = "algebraic-geometry-foundations/affine-line"
title = "Affine line"
kind = "knowl"
summary = "The affine scheme Spec(k[x]) representing one algebraic coordinate over a base field."
aliases = ["affine-line", "Affine line"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/affine-scheme", "algebra-rings/polynomial-ring", "algebra-rings/prime-ideal", "algebraic-geometry-foundations/closed-point", "algebraic-geometry-foundations/algebraically-closed-field", "algebraic-geometry-foundations/generic-point", "topology/irreducible-space"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "algebraic-geometry-foundations/affine-line.md"
+++

Let \(k\) be a field. The **affine line over \(k\)** is the [[algebraic-geometry-foundations/affine-scheme|affine scheme]]
\[
\mathbb A_k^1:=\operatorname{Spec}k[x],
\]
where \(k[x]\) is the [[algebra-rings/polynomial-ring|polynomial ring]] in one variable. Its points are all [[algebra-rings/prime-ideal|prime ideals]] of \(k[x]\), not only elements of \(k\).

Each \(a\in k\) determines the [[algebraic-geometry-foundations/closed-point|closed point]] \((x-a)\). If \(k\) is [[algebraic-geometry-foundations/algebraically-closed-field|algebraically closed]], these are exactly the closed points, while \((0)\) is a [[algebraic-geometry-foundations/generic-point|generic point]] whose closure is all of \(\mathbb A_k^1\). Thus the scheme-theoretic affine line contains the familiar coordinate line together with extra information about [[topology/irreducible-space|irreducibility]] and specialization.

## Examples

For example, the basic Zariski open subset \(D(x)\) removes the origin. Its ring of regular functions is \(k[x,x^{-1}]\), so \(x\) becomes invertible there. The higher-dimensional version is [[algebraic-geometry-foundations/affine-n-space|affine \(n\)-space]].
