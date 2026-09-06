+++
id = "functional-analysis/graph-of-operator"
title = "Graph of a linear operator"
kind = "definition"
summary = "The subspace of a product space consisting of each domain vector paired with its image."
aliases = ["operator graph"]
domains = ["functional-analysis", "linear-algebra"]
prerequisites = ["linear-algebra/vector-space", "convex-analysis/linear-subspace", "topology/product-topology"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(T:D(T)\subseteq X\to Y\) be a linear operator between [[linear-algebra/vector-space|vector spaces]]. Its **graph** is the [[convex-analysis/linear-subspace|linear subspace]]
\[
\mathcal G(T)=\{(x,Tx):x\in D(T)\}\subseteq X\times Y.
\]
The graph records both the action of \(T\) and its domain: the first-coordinate projection maps \(\mathcal G(T)\) bijectively onto \(D(T)\), and \(T\) is recovered by following its inverse with the second-coordinate projection. For a [[functional-analysis/densely-defined-operator|densely defined operator]], density concerns \(D(T)\), while closedness and closability concern \(\mathcal G(T)\) inside the [[topology/product-topology|product topology]].

## Closedness and closability

If \(X\) and \(Y\) are [[linear-algebra/banach-space|Banach spaces]], \(T\) is closed exactly when \(\mathcal G(T)\) is closed in \(X\times Y\). Equivalently, whenever \(x_n\to x\) and \(Tx_n\to y\), one has \(x\in D(T)\) and \(Tx=y\). The operator is closable exactly when the closure of \(\mathcal G(T)\) is itself the graph of an operator; that operator is the closure \(\overline T\).

## Graph norm

When \(X\) and \(Y\) are normed spaces, the [[functional-analysis/graph-norm|graph norm]] on \(D(T)\) may be defined by
\[
\|x\|_T=\|x\|_X+\|Tx\|_Y.
\]
The map \(x\mapsto(x,Tx)\) identifies this normed space with the graph equipped with the corresponding product norm. If \(X\) and \(Y\) are Banach spaces, \(T\) is closed precisely when \(D(T)\) is complete in the graph norm.

## Why the domain matters

The same formula can define different operators when assigned different domains, and their graphs then differ. For example, differentiation on \(L^2\) has distinct closed realizations determined by boundary conditions. Graph language makes this domain dependence explicit and is therefore essential for unbounded operators.

## References

1. Tosio Kato, *Perturbation Theory for Linear Operators*, 2nd ed., Springer, 1976. [DOI record](https://doi.org/10.1007/978-3-642-66282-9). Relevant: Chapter III on closed operators and their graphs.
2. Konrad Schmüdgen, *Unbounded Self-adjoint Operators on Hilbert Space*, Springer, 2012. [DOI record](https://doi.org/10.1007/978-94-007-4753-1). Relevant: Chapter 1 on domains, graphs, and closures.
