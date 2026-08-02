+++
id = "functional-analysis/densely-defined-operator"
title = "Densely defined operator"
kind = "definition"
summary = "A linear operator whose specified domain is dense in its ambient Hilbert space."
aliases = ["densely defined linear operator", "operator with dense domain"]
domains = ["functional-analysis"]
section_mode = "progressive"
+++

Let \(H\) and \(K\) be [[linear-algebra/hilbert-space|Hilbert spaces]]. A **densely defined operator from \(H\) to \(K\)** is a pair \((D(T),T)\), where \(D(T)\) is a [[convex-analysis/linear-subspace|linear subspace]] of \(H\), [[topology/dense-set|dense]] in \(H\), and
\[
T:D(T)\longrightarrow K
\]
is a [[linear-algebra/linear-map|linear map]]. The domain \(D(T)\) is part of the operator: two maps given by the same formula on different domains are different operators. When \(H=K\), one says that \(T\) is an operator in \(H\). No boundedness, continuity, or closedness is assumed.

## The adjoint

Density is precisely what makes an adjoint single-valued. Using [[linear-algebra/inner-product|inner products]] linear in the first variable, \(y\in K\) belongs to \(D(T^*)\) when there is \(z\in H\) such that
\[
\langle Tx,y\rangle_K=\langle x,z\rangle_H
\]
for every \(x\in D(T)\); then \(T^*y=z\). The vector \(z\) is unique because \(D(T)\) is dense. The adjoint is always closed, although its own domain need not be dense.

## Graph, closure, and examples

The graph of \(T\) is the linear subspace \(\{(x,Tx):x\in D(T)\}\subseteq H\oplus K\). The operator is [[functional-analysis/closed-linear-operator|closed]] when this graph is closed, and closable when its graph closure is again the graph of an operator. On an [[measure-theory/lp-space|\(L^2\)-space]], differentiation on smooth compactly supported functions and multiplication by an unbounded [[measure-theory/measurable-function|measurable function]] are standard densely defined operators. Their domains cannot be discarded without changing their adjoints and closures.

## Conventions and scope

**Warning.** “Densely defined” does not mean “defined everywhere,” and it implies neither boundedness nor self-adjointness. An everywhere-defined closed operator between [[linear-algebra/banach-space|Banach spaces]] is bounded, but unbounded closed operators avoid that conclusion by having proper domains.

## References

1. K. Schmüdgen, *Unbounded Self-adjoint Operators on Hilbert Space*, Springer, 2012. [Springer DOI record](https://doi.org/10.1007/978-94-007-4753-1). Relevant: Chapter 1, “Basics of Closed Operators.”
