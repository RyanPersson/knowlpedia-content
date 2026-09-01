+++
id = "algebra-hyperstructures/hyperoperation"
title = "Hyperoperation"
kind = "definition"
summary = "A binary operation whose value is a nonempty set of possible outputs."
aliases = ["multivalued operation", "binary hyperoperation"]
domains = ["algebra-hyperstructures", "algebra-rings"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A **binary hyperoperation** on a set \(X\) is a map
\[
\boxplus:X\times X\longrightarrow \mathcal P^*(X),
\]
where \(\mathcal P^*(X)\) is the collection of nonempty subsets of \(X\).
Thus \(x\boxplus y\) is a nonempty set of possible sums, not one chosen
element.

## Extension to subsets

For nonempty subsets \(A,B\subseteq X\), extend the operation by
\[
A\boxplus B=\bigcup_{a\in A,\,b\in B}(a\boxplus b).
\]
Expressions such as \((a\boxplus b)\boxplus c\) use this extension.
Associativity means equality of subsets
\((a\boxplus b)\boxplus c=a\boxplus(b\boxplus c)\), not merely that the two
subsets intersect.

## Ordinary operations as a special case

An ordinary [[shared-foundations/binary-operation|binary operation]] \(*\) determines the singleton-valued
hyperoperation \(a\boxplus b=\{a*b\}\). Hyperoperations therefore include
ordinary operations, but a genuinely multivalued operation cannot be treated
as a function \(X\times X\to X\) without discarding information.

## References

1. Matthew Baker and Nathan Bowler, “Matroids over hyperfields,” 2017. [arXiv:1601.01204](https://arxiv.org/abs/1601.01204). Relevant: §2, hyperoperations and hypergroups.
2. Oleg Viro, “Hyperfields for Tropical Geometry I: Hyperfields and dequantization,” 2010. [arXiv:1006.3034](https://arxiv.org/abs/1006.3034). Relevant: §3, multivalued addition.
