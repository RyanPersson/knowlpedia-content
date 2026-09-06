+++
id = "functional-analysis/closable-operator"
title = "Closable operator"
kind = "definition"
summary = "A linear operator whose graph closure is still the graph of an operator."
aliases = ["preclosed operator"]
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/hilbert-space", "functional-analysis/graph-of-operator", "functional-analysis/closed-linear-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(T:\operatorname{Dom}(T)\subseteq H\to K\) be a linear operator between
[[linear-algebra/hilbert-space|Hilbert spaces]]; its domain need not be all of \(H\). The operator \(T\) is
**closable** if the closure of its
[[functional-analysis/graph-of-operator|graph]] in \(H\oplus K\) is the graph
of an operator. That operator is denoted \(\overline T\), called the
**closure** of \(T\), and is the smallest
[[functional-analysis/closed-linear-operator|closed operator]] extending
\(T\). Equivalently, whenever \(x_n\in\operatorname{Dom}(T)\),
\(x_n\to0\), and \(Tx_n\to y\), one must have \(y=0\). This criterion prevents
the graph closure from assigning two different values to the same input.

## Characterizations by extensions

An operator is closable exactly when it has at least one closed extension. If
\(S\) is any closed extension of \(T\), then
\(\overline T\subseteq S\), including containment of domains. An operator is
already closed precisely when \(T=\overline T\). These statements concern
graph closure, not merely closure of \(\operatorname{Dom}(T)\) in \(H\).

## Adjoint criterion

If \(T\) is densely defined, its Hilbert-space adjoint \(T^*\) is closed, and
\[
T\text{ is closable}\quad\Longleftrightarrow\quad
\operatorname{Dom}(T^*)\text{ is dense in }K.
\]
In that case \(\overline T=T^{**}\). Density of the original domain is needed
to define \(T^*\) as an operator, but it is not needed for the graph-based
definition of closability itself.

## Examples and a non-example

The derivative \(d/dx\) on \(C_c^\infty(0,1)\subset L^2(0,1)\) is closable;
its closure has domain \(H_0^1(0,1)\). By contrast, let \(T:c_{00}\subset
\ell^2\to\ell^2\) satisfy \(Te_n=n e_1\). Then
\(x_n=e_n/n\to0\) but \(Tx_n=e_1\), so \(T\) is not closable. This example
shows that a [[functional-analysis/densely-defined-operator|densely defined linear operator]] need not be closable.

## References

1. Tosio Kato, Perturbation Theory for Linear Operators, 2nd ed., corrected reprint, Springer, 1995. [DOI record](https://doi.org/10.1007/978-3-642-66282-9). Relevant: Chapter III, §5 on closed and closable operators.
2. Konrad Schmüdgen, Unbounded Self-adjoint Operators on Hilbert Space, Springer, 2012. [DOI record](https://doi.org/10.1007/978-94-007-4753-1). Relevant: Chapter 1 on graphs, closures, and adjoints.
