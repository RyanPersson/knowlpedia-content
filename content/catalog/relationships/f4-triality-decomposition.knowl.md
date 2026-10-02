+++
id = "catalog/relationships/f4-triality-decomposition"
title = "Triality decomposition of compact f4"
kind = "theorem"
summary = "Restriction to Spin(8) splits compact f4 into its adjoint and three eight-dimensional modules."
aliases = ["Triality decomposition of compact f4"]
domains = ["catalog", "lie-groups", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["catalog/lie-algebras/f4-compact", "nonassociative-algebra/exceptional-jordan-algebra", "lie-groups/spin8-triality", "lie-groups/lie-subalgebra"]
dependency_heuristic = "catalog-semantic-author-review-v1"
dependency_review_count = 1
+++

For the compact real [[catalog/lie-algebras/f4-compact|Lie algebra \(\mathfrak f_4\)]], the \(\operatorname{Spin}(8)\) subgroup fixing a labelled frame in the [[nonassociative-algebra/exceptional-jordan-algebra|Albert algebra]] gives a module decomposition
\[
\mathfrak f_4\cong\mathfrak{so}(8)\oplus8_v\oplus8_+\oplus8_-.
\]
The \(\mathfrak{so}(8)\) summand is a [[lie-groups/lie-subalgebra|Lie subalgebra]] and has its adjoint action. The other summands are the three inequivalent real eight-dimensional representations linked by [[lie-groups/spin8-triality|triality]]. This is a decomposition of representations, not of Lie ideals.

## Dimensions and the Albert algebra

The dimensions add to \(28+8+8+8=52\). The same three modules occur in the off-diagonal entries of \(H_3(\mathbb O)\), whose decomposition under the [[nonassociative-algebra/spin8-stabilizer-of-an-albert-algebra-frame|frame stabilizer]] is
\[
H_3(\mathbb O)\cong\mathbb R^3\oplus8_v\oplus8_+\oplus8_-.
\]
These are different representations: the three diagonal lines in the Albert algebra are fixed, while the \(28\)-dimensional summand above is adjoint.

## References

1. John C. Baez, “The Octonions,” §4.2, the decomposition into so(8) and its three eight-dimensional modules. [Checked section](https://math.ucr.edu/home/baez/octonions/node15.html).
2. John C. Baez, “The Octonions,” §3.4, the triality description of the Albert algebra. [Checked section](https://math.ucr.edu/home/baez/octonions/node12.html).
