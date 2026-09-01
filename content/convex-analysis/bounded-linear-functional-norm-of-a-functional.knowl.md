+++
id = "convex-analysis/bounded-linear-functional-norm-of-a-functional"
title = "Bounded Linear Functional and Its Norm"
kind = "knowl"
summary = "A linear functional is bounded exactly when it is continuous; its norm is the supremum of its absolute value on the unit ball."
aliases = ["bounded-linear-functional-norm-of-a-functional", "Bounded Linear Functional and Its Norm"]
domains = ["convex-analysis"]
prerequisites = ["convex-analysis/norm-normed-vector-space", "convex-analysis/linear-operator-linear-transformation"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
legacy_source_path = "convex-analysis/bounded-linear-functional-norm-of-a-functional.md"
+++

Let \(X\) be a [[convex-analysis/norm-normed-vector-space|normed space]] over \(\mathbb K\in\{\mathbb R,\mathbb C\}\). A [[convex-analysis/linear-operator-linear-transformation|linear map]] \(f:X\to\mathbb K\) is a **linear functional**. It is **bounded** if there exists \(M\ge0\) such that
\[
|f(x)|\le M\lVert x\rVert\qquad\text{for every }x\in X.
\]

Its **operator norm** is
\[
\lVert f\rVert=\sup_{\lVert x\rVert\le1}|f(x)|.
\]

## Equivalent characterizations

Equivalently,
\[
\lVert f\rVert=\inf\{M\ge0:|f(x)|\le M\lVert x\rVert\text{ for every }x\in X\}.
\]
Boundedness is equivalent to continuity.

## Remarks

This notion is used in [[convex-analysis/hahn-banach-theorem-in-normed-spaces|Hahn–Banach in normed spaces]] and in separation results such as [[convex-analysis/separation-of-a-point-and-a-subspace|separating a point and a subspace]].

## Examples

- On \(X=\mathbb R^n\) with the Euclidean norm, \(f(x)=\langle a,x\rangle\) has norm \(\lVert a\rVert_2\).
- On \(C[0,1]\) with the supremum norm, evaluation \(f(x)=x(t_0)\) has norm \(1\).
