+++
id = "functional-analysis/rank-one-operator"
title = "Rank-one operator"
kind = "definition"
summary = "A bounded linear operator whose range is a one-dimensional vector space."
aliases = ["operator of rank one"]
domains = ["functional-analysis", "linear-algebra"]
section_mode = "progressive"
prerequisites = ["functional-analysis/bounded-linear-operator", "linear-algebra/linear-map", "linear-algebra/normed-vector-space", "convex-analysis/basis-hamel-basis-and-dimension"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 2
+++

Let \(X\) and \(Y\) be [[linear-algebra/normed-vector-space|normed vector spaces]] over the same field, \(\mathbb R\) or \(\mathbb C\). A **rank-one operator** is a [[functional-analysis/bounded-linear-operator|bounded linear operator]] \(T:X\to Y\) such that \(\dim T(X)=1\).

## Representation

Every rank-one operator can be written
\[
Tx=\varphi(x)y,
\]
where \(y\in Y\) is nonzero and \(\varphi:X\to\mathbb F\) is a nonzero [[convex-analysis/bounded-linear-functional-norm-of-a-functional|bounded linear functional]]. Conversely, every such formula defines a rank-one operator. Its range is the line spanned by \(y\).

## Scope

The zero operator has rank zero and is therefore not rank one.

Rank one here refers to the dimension of the linear range. In Hilbert \(C^*\)-module theory, a “rank-one operator” can instead mean \(\theta_{y,x}(z)=y\langle x,z\rangle\); that Hilbert-module convention is defined by [[operator-algebras/compact-operator-hilbert-module|compact operators on Hilbert modules]] and need not have one-dimensional range.

## References

1. John B. Conway, *A Course in Functional Analysis*, 2nd ed., Springer, 1990. [Springer DOI record](https://doi.org/10.1007/978-1-4757-4383-8). Relevant: Chapter II, finite-rank operators.
