+++
id = "linear-algebra/operator-invariant-subspace"
title = "Invariant subspace of an operator"
kind = "knowl"
summary = "A linear subspace mapped into itself by a linear operator."
aliases = ["invariant subspace", "operator-invariant subspace"]
domains = ["linear-algebra", "analysis"]
prerequisites = ["linear-algebra/linear-map", "linear-algebra/closed-linear-subspace", "linear-algebra/eigenvector"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(T:E\to E\) be a [[linear-algebra/linear-map|linear operator]]. A linear subspace \(M\subseteq E\) is **invariant under \(T\)** if
\[
T(M)\subseteq M.
\]
The invariant subspace is **nontrivial** when \(M\ne\{0\}\) and \(M\ne E\). In functional analysis one usually also requires \(M\) to be a [[linear-algebra/closed-linear-subspace|closed linear subspace]].

If \(v\) is an [[linear-algebra/eigenvector|eigenvector]] of \(T\), then its one-dimensional span is invariant. Invariance also means that \(T\) restricts to a well-defined operator \(T|_M:M\to M\).
