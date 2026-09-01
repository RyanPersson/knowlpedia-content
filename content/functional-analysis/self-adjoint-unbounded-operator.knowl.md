+++
id = "functional-analysis/self-adjoint-unbounded-operator"
title = "Self-adjoint unbounded operator"
kind = "definition"
summary = "A densely defined Hilbert-space operator is self-adjoint when it equals its adjoint both in action and in domain."
aliases = ["self-adjoint operator with domain", "unbounded Hermitian operator"]
domains = ["functional-analysis"]
prerequisites = ["linear-algebra/hilbert-space", "functional-analysis/adjoint-unbounded-operator", "functional-analysis/closed-linear-operator"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(H\) be a [[linear-algebra/hilbert-space|Hilbert space]] and let \(A:\mathcal D(A)\subseteq H\to H\) be densely defined. In the unbounded-operator setting, \(A\) is **self-adjoint** when
\[
A=A^*,
\]
meaning both \(\mathcal D(A)=\mathcal D(A^*)\) and \(Ax=A^*x\) for every vector in that common domain, where \(A^*\) is the [[functional-analysis/adjoint-unbounded-operator|adjoint of a densely defined operator]]. No boundedness is assumed. Equality of the operator formulas without equality of their domains is insufficient. Every self-adjoint operator is a [[functional-analysis/closed-linear-operator|closed linear operator]] and, in particular, has a dense domain.

## Equivalent characterizations

A densely defined [[functional-analysis/symmetric-operator|symmetric operator]] \(A\) is self-adjoint if and only if
\[
\operatorname{Ran}(A+iI)=H=\operatorname{Ran}(A-iI).
\]
Equivalently, its deficiency subspaces \(\ker(A^*-iI)\) and \(\ker(A^*+iI)\) both vanish.

## Spectral consequences

The spectrum of a self-adjoint operator is real, and \(A-zI\) has a bounded inverse for every nonreal \(z\). The spectral theorem then supplies projection-valued functional calculus, making self-adjoint operators the appropriate mathematical model for possibly unbounded observables.

## Example and boundary case

On \(L^2(\mathbb R)\), multiplication by the coordinate,
\[
(Af)(x)=xf(x),\qquad \mathcal D(A)=\{f\in L^2(\mathbb R):xf\in L^2(\mathbb R)\},
\]
is self-adjoint and unbounded. Restricting the same formula to a smaller dense domain may produce only a symmetric operator; the domain is therefore part of the operator, not bookkeeping.

## References

1. Konrad Schmüdgen, *Unbounded Self-adjoint Operators on Hilbert Space*, Graduate Texts in Mathematics 265, Springer, 2012. [DOI record](https://doi.org/10.1007/978-94-007-4753-1). Relevant: chapter 1 on closed, adjoint, symmetric, and self-adjoint operators.
2. Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, revised edition, Academic Press, 1980. [Publisher record](https://www.sciencedirect.com/book/9780125850506/functional-analysis). Relevant: chapter VIII on unbounded operators.
