+++
id = "topology/finite-intersection-property"
title = "Finite intersection property"
kind = "knowl"
summary = "A property of a family of sets where every finite subfamily has nonempty intersection."
aliases = ["finite-intersection-property", "Finite intersection property"]
domains = ["topology"]
legacy_source_path = "topology/finite-intersection-property.md"
prerequisites = ["topology/closed-set", "topology/compact-set"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A family \(\mathcal F\) of subsets of a set \(X\) has the **finite intersection property** if every finite subfamily has nonempty intersection. In particular, for \(F_1,\ldots,F_n\in\mathcal F\),
\[
F_1\cap\cdots\cap F_n \neq \varnothing,
\]
In topology, the finite intersection property is especially useful for families of [[topology/closed-set|closed sets]]: [[topology/compact-set|compactness]] can be characterized by requiring that every family of closed sets with this property has nonempty total intersection.

## Examples

- In \(\mathbb R\), the family \(F_n=[n,\infty)\) has the finite intersection property, but \(\bigcap_{n\ge1}F_n=\varnothing\).
- The family \(\{\{1,2\},\{2,3\},\{2,4\}\}\) has the finite intersection property because every finite intersection contains \(2\).
