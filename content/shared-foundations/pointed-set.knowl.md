+++
id = "shared-foundations/pointed-set"
title = "Pointed set"
kind = "definition"
summary = "A set equipped with a distinguished element called its basepoint."
aliases = ["based set", "set with basepoint", "pointed object in Set"]
domains = ["shared-foundations", "category-theory", "topology"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A **pointed set** is a pair \((X,x_0)\) consisting of a set \(X\) and a
distinguished element \(x_0\in X\), called the **basepoint**. A morphism of
pointed sets \(f:(X,x_0)\to(Y,y_0)\) is a function satisfying
\(f(x_0)=y_0\).

## Examples

Any group is a pointed set with its identity as basepoint, but a pointed set
need not carry a multiplication. Nonabelian cohomology sets are commonly
pointed by the class of the trivial cocycle or trivial bundle.

## Categorical description

The category of pointed sets is equivalent to the coslice category
\(\{*\}\!\downarrow\!\mathbf{Set}\): selecting a map from a singleton to
\(X\) is the same as selecting one element of \(X\).

## References

1. Saunders Mac Lane, *Categories for the Working Mathematician*, 2nd ed., Springer, 1998. [DOI record](https://doi.org/10.1007/978-1-4757-4721-8). Relevant: pointed objects and comma categories.
