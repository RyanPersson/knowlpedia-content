+++
id = "convex-analysis/separation-of-a-point-and-a-subspace"
title = "Separation of a Point and a Subspace"
kind = "knowl"
summary = "If a point has positive distance to a subspace, a bounded functional separates them."
aliases = ["separation-of-a-point-and-a-subspace", "Separation of a Point and a Subspace"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/separation-of-a-point-and-a-subspace.md"
+++

**Separation theorem.** Let \(X\) be a normed space over \(\mathbb K\in\{\mathbb R,\mathbb C\}\), let \(Y\subseteq X\) be a [[convex-analysis/linear-subspace|linear subspace]], and suppose \(x_0\in X\) has positive distance
\[
d(x_0,Y):=\inf_{y\in Y}\|x_0-y\|=d>0.
\]
Then there exists a [[convex-analysis/bounded-linear-functional-norm-of-a-functional|bounded linear functional]] \(f:X\to\mathbb K\) such that
\[
f|_Y=0,\qquad f(x_0)=1,\qquad \lVert f\rVert=\frac1d.
\]

## Proof idea

On \(Y\oplus\operatorname{span}\{x_0\}\), define \(f_0(y+\lambda x_0)=\lambda\). The distance assumption gives \(\lVert f_0\rVert=1/d\), and [[convex-analysis/hahn-banach-theorem-in-normed-spaces|Hahn–Banach]] extends \(f_0\) to \(X\) without increasing its norm.
