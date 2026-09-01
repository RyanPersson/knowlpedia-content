+++
id = "functional-analysis/graph-norm"
title = "Graph norm"
kind = "definition"
summary = "The norm on an operator domain that controls both a vector and its image."
aliases = ["operator graph norm"]
domains = ["functional-analysis"]
prerequisites = ["linear-algebra/normed-vector-space", "functional-analysis/graph-of-operator"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(T:D(T)\subseteq X\to Y\) be a linear operator between [[linear-algebra/normed-vector-space|normed vector spaces]]. The **graph norm** of \(T\) is the norm on \(D(T)\) defined by
\[
\lVert x\rVert_T=\lVert x\rVert_X+\lVert Tx\rVert_Y.
\]
Equivalently, it is the norm transported from the [[functional-analysis/graph-of-operator|graph of \(T\)]] by the linear bijection \(x\mapsto(x,Tx)\), when \(X\times Y\) is given the sum norm. The graph norm is stronger than the norm inherited from \(X\): convergence \(x_n\to x\) in graph norm means both \(x_n\to x\) in \(X\) and \(Tx_n\to Tx\) in \(Y\).

## Completeness and closedness

If \(X\) and \(Y\) are [[linear-algebra/banach-space|Banach spaces]], then \(T\) is closed exactly when \((D(T),\lVert\cdot\rVert_T)\) is a Banach space. Indeed, the graph map identifies the operator domain isometrically with \(\Gamma(T)\subseteq X\times Y\), and a [[convex-analysis/linear-subspace|linear subspace]] of a Banach space is complete precisely when it is closed.

## Equivalent choices

When \(X\) and \(Y\) are [[linear-algebra/hilbert-space|Hilbert spaces]], one often uses
\[
\lVert x\rVert_{T,2}
=\bigl(\lVert x\rVert_X^2+\lVert Tx\rVert_Y^2\bigr)^{1/2}.
\]
This norm is equivalent to the sum graph norm and comes from the graph [[linear-algebra/inner-product|inner product]]
\[
\langle x,z\rangle_T=\langle x,z\rangle_X+\langle Tx,Tz\rangle_Y.
\]
The two formulas define the same topology on \(D(T)\), though only the second is induced by an inner product.

## Cores

For a [[functional-analysis/closed-linear-operator|closed operator]] \(T\), a subspace \(D_0\subseteq D(T)\) is a **core** when it is dense in \(D(T)\) for the graph norm. Equivalently, the restriction \(T|_{D_0}\) is closable and its closure is \(T\). Ordinary density of \(D_0\) in \(X\) is not enough, because it does not control convergence of the images \(Tx\).

## References

1. Tosio Kato, *Perturbation Theory for Linear Operators*, Springer, 1995 reprint of the 2nd ed. [Springer DOI record](https://doi.org/10.1007/978-3-642-66282-9). Relevant: Chapter III.
2. Konrad Schmüdgen, *Unbounded Self-adjoint Operators on Hilbert Space*, Springer, 2012. [Springer DOI record](https://doi.org/10.1007/978-94-007-4753-1). Relevant: Chapter 1.
