+++
id = "convex-analysis/linear-subspace"
title = "Linear subspace"
kind = "knowl"
summary = "A subset containing zero and closed under addition and scalar multiplication."
aliases = ["linear-subspace", "Linear subspace"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/linear-subspace.md"
prerequisites = ["linear-algebra/vector-space"]
dependency_heuristic = "semantic-curriculum-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a vector space over a field \(K\), and let \(Y\subseteq X\). The set \(Y\) is a **linear subspace** of \(X\) if

1. \(0\in Y\),
2. \(a+b\in Y\) for all \(a,b\in Y\), and
3. \(\lambda a\in Y\) for all \(\lambda\in K\) and \(a\in Y\).

With the inherited operations, \(Y\) is itself a [[linear-algebra/vector-space|vector space]].

## Examples

- \(\{0\}\) and \(X\) are subspaces of \(X\).
- In the vector space of all scalar sequences, \(\ell^1=\{x=(x_n):\sum_{n=1}^\infty|x_n|<\infty\}\) is a subspace.
- The continuous functions \(C([a,b])\) form a subspace of all functions \([a,b]\to K\).
