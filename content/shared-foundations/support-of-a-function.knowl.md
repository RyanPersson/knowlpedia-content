+++
id = "shared-foundations/support-of-a-function"
title = "Support of a function"
kind = "definition"
summary = "The closure of the set on which a function is nonzero."
aliases = ["function support", "support of a scalar function"]
domains = ["shared-foundations", "topology", "analysis"]
prerequisites = []
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(f:X\to\mathbb F\) be a function on a topological space, where
\(\mathbb F\) has a distinguished zero element. The **support of \(f\)** is

\[
\operatorname{supp}(f)=\overline{\{x\in X:f(x)\ne0\}}.
\]

Thus the support is a closed subset of \(X\), and \(f\) vanishes on its
complement.

## Why the closure is included

The nonzero set need not be closed. Taking its closure includes boundary
points at which \(f\) may vanish but arbitrarily nearby values are nonzero.
This convention makes compact support mean that this closed set is compact.

## Uses

Families of supports appear in the local-finiteness condition for partitions
of unity. Supports also localize test functions, sections, distributions, and
other analytic objects, whose specialized notions of support extend this
definition.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: supports, bump functions, and partitions of unity.
