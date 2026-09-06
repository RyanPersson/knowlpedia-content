+++
id = "functional-analysis/closed-linear-operator"
title = "Closed linear operator"
kind = "definition"
summary = "A possibly unbounded linear operator whose graph is closed in the product space."
aliases = ["closed operator"]
domains = ["functional-analysis"]
prerequisites = ["linear-algebra/normed-vector-space", "convex-analysis/linear-subspace", "functional-analysis/graph-of-operator", "topology/closed-set"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(X\) and \(Y\) be [[linear-algebra/normed-vector-space|normed vector spaces]], and let \(T:D(T)\subseteq X\to Y\) be linear on the [[convex-analysis/linear-subspace|linear subspace]] \(D(T)\). The operator \(T\) is **closed** if its [[functional-analysis/graph-of-operator|graph]]
\[
\Gamma(T)=\{(x,Tx):x\in D(T)\}
\]
is a [[topology/closed-set|closed set]] in \(X\times Y\). Equivalently, whenever \(x_n\in D(T)\), \(x_n\to x\) in \(X\), and \(Tx_n\to y\) in \(Y\), one has \(x\in D(T)\) and \(Tx=y\). Closedness constrains simultaneous convergence of inputs and outputs; it neither says that \(D(T)\) is closed in \(X\) nor implies that \(T\) is bounded on \(D(T)\) with the norm inherited from \(X\).

## Closed versus bounded

The [[functional-analysis/closed-graph-theorem|closed graph theorem]] says that a closed linear operator \(T:X\to Y\) defined on all of a [[linear-algebra/banach-space|Banach space]] \(X\), with \(Y\) Banach, is bounded. Properly defined closed operators can be unbounded. Differential operators on \(L^p\)- or [[linear-algebra/hilbert-space|Hilbert spaces]] are principal examples: their domains encode the regularity and boundary conditions needed for the graph to be closed.

## Closure and closability

An operator is **closable** if the closure of \(\Gamma(T)\) is itself the graph of an operator. This happens exactly when
\[
x_n\to0,\quad Tx_n\to y
\quad\Longrightarrow\quad y=0.
\]
The operator whose graph is \(\overline{\Gamma(T)}\) is the closure \(\overline T\), the smallest closed extension of \(T\). Hence “closed” and “closable” are not synonyms.

## Domain-sensitive operations

For unbounded operators, algebraic expressions have domain conditions. The product \(ST\) is defined only on those \(x\in D(T)\) for which \(Tx\in D(S)\), and a sum requires a common domain. Closed operators are therefore not automatically preserved by sums or products. Statements about adjoints, resolvents, or self-adjointness must likewise include density and domain hypotheses.

## References

1. Tosio Kato, *Perturbation Theory for Linear Operators*, Springer, 1995 reprint of the 2nd ed. [Springer DOI record](https://doi.org/10.1007/978-3-642-66282-9). Relevant: Chapter III.
2. Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics, Volume I: Functional Analysis*, Academic Press, 1980. [Elsevier book record](https://shop.elsevier.com/books/methods-of-modern-mathematical-physics/reed/978-0-12-585001-8). Relevant: Chapter VIII.
