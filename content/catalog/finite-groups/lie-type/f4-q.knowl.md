+++
id = "catalog/finite-groups/lie-type/f4-q"
title = "F₄(q)"
kind = "definition"
summary = "The finite Chevalley group of type F₄, with its finite center divided out."
aliases = []
domains = ["catalog", "algebra-groups"]
prerequisites = ["catalog/finite-groups/lie-type/finite-chevalley-central-quotient", "algebraic-geometry-foundations/algebraic-group"]
dependency_heuristic = "finite-lie-type-core-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For a prime power \(q\geq 2\), \(F_4(q)\) is the [[catalog/finite-groups/lie-type/finite-chevalley-central-quotient|finite Chevalley central quotient]] of type \(F_4\):
\[
 F_4(q)=\mathbf G_{F_4,\mathrm{sc}}(\mathbb F_{q})/Z\bigl(\mathbf G_{F_4,\mathrm{sc}}(\mathbb F_{q})\bigr).
\]
Here \(\mathbf G_{F_4,\mathrm{sc}}\) is the split simply connected [[algebraic-geometry-foundations/algebraic-group|algebraic group]] of the displayed root-system type. Its finite points are fixed by coordinatewise \(q\)-power Frobenius, and multiplication is multiplication of cosets of their finite center.

## Order and simplicity

Its order is
\[ |F_4(q)|=q^{24}(q^{2}-1)(q^{6}-1)(q^{8}-1)(q^{12}-1). \]

It is a nonabelian [[algebra-groups/simple-group|simple group]] for every admitted prime power q.

## Rank and central quotient

The absolute rank is \(4\). The finite center of the simply connected group has order \(1\); the notation here always denotes the quotient by that center. There are no omitted small-field simplicity exceptions for this type.

## References

1. [Robert Steinberg, Lectures on Chevalley Groups (Yale, 1967)](https://www.math.utah.edu/~ptrapa/math-library/steinberg/steinberg-yale-notes.pdf), §3 construction; §4 Theorem 5, PDF pp. 52–54; §9 Theorems 24–25, PDF pp. 136–138.
2. [B. Akbari, ODs-characterization of some low-dimensional finite classical groups](https://www.ieja.net/files/papers/volume-24/8-V24-2018.pdf), Table 2, p. 85: order column only; its additional Restrictions concern a separate invariant.
