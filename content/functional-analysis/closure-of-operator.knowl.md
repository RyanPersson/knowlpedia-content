+++
id = "functional-analysis/closure-of-operator"
title = "Closure of a closable operator"
kind = "definition"
summary = "The minimal closed extension obtained by closing the graph of a closable operator."
aliases = ["operator closure", "minimal closed extension"]
domains = ["functional-analysis", "operator-theory"]
prerequisites = ["functional-analysis/closable-operator", "linear-algebra/banach-space", "functional-analysis/graph-of-operator", "functional-analysis/closed-linear-operator"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(T:\mathcal D(T)\subseteq X\to Y\) be a
[[functional-analysis/closable-operator|closable operator]] between
[[linear-algebra/banach-space|Banach spaces]]. Its **closure** \(\overline T\)
is the operator whose [[functional-analysis/graph-of-operator|graph]] is the
closure of the graph of \(T\) in \(X\times Y\):
\[
\mathcal G(\overline T)=\overline{\mathcal G(T)}.
\]
Equivalently, \(x\in\mathcal D(\overline T)\) precisely when some sequence
\(x_n\in\mathcal D(T)\) satisfies \(x_n\to x\) and \(Tx_n\to y\) for some
\(y\in Y\); then \(\overline Tx=y\). Closability is exactly what makes this
limit \(y\) unique. The operator \(\overline T\) is
[[functional-analysis/closed-linear-operator|closed]], extends \(T\), and is
contained in every closed extension of \(T\).

## Graph characterization

The closure operation adds exactly the limit pairs forced by the original
graph. In particular,
\[
\mathcal D(\overline T)
=\left\{x:\exists x_n\in\mathcal D(T),\
x_n\to x,\ (Tx_n)\text{ converges}\right\}.
\]
The value of \(\overline T\) is determined by the limit of \(Tx_n\), and does
not depend on the chosen approximating sequence. If the closed graph contains
a nonzero pair \((0,y)\), no operator can have that graph and \(T\) is not
closable.

## Relation to adjoints

For a [[functional-analysis/densely-defined-operator|densely defined
operator]] between [[linear-algebra/hilbert-space|Hilbert spaces]], \(T\) is closable exactly when the domain
of its
[[functional-analysis/adjoint-unbounded-operator|adjoint]] \(T^*\) is dense.
In that case,
\[
\overline T=T^{**}.
\]
This identity includes the domains: it is not merely equality of the formal
actions. The adjoint \(T^*\) itself is always closed.

## Example and warning

On \(L^2(\mathbb R)\), restrict multiplication by the coordinate \(x\) to
[[functional-analysis/test-function-space|compactly supported smooth functions]]. Its closure is the maximal
multiplication operator
\[
(\overline Tf)(x)=xf(x),\qquad
\mathcal D(\overline T)=\{f\in L^2(\mathbb R):xf\in L^2(\mathbb R)\}.
\]
Other closed extensions can exist, especially for differential operators
with boundary conditions. The closure is the smallest closed extension, not
an arbitrarily chosen [[functional-analysis/self-adjoint-extension|self-adjoint extension]].

## References

- [Konrad Schmüdgen, *Unbounded Self-adjoint Operators on Hilbert Space*, Chapter 1 (Springer, 2012)](https://doi.org/10.1007/978-94-007-4753-1)
- [Tosio Kato, *Perturbation Theory for Linear Operators*, Chapter III, §5 (Springer, 1995)](https://doi.org/10.1007/978-3-642-66282-9)
