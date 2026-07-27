+++
id = "functional-analysis/symmetric-operator"
title = "Symmetric operator"
kind = "definition"
summary = "A symmetric operator is a densely defined Hilbert-space operator whose inner products agree with those of its adjoint on its own domain."
aliases = ["Hermitian operator on a dense domain", "formally symmetric operator"]
domains = ["functional-analysis"]
section_mode = "progressive"
+++

Let \(H\) be a [[linear-algebra/hilbert-space|Hilbert space]]. A [[functional-analysis/densely-defined-operator|densely defined linear operator]] \(A:\mathcal D(A)\subseteq H\to H\) is **symmetric** when
\[
\langle Ax,y\rangle=\langle x,Ay\rangle
\]
for every \(x,y\in\mathcal D(A)\). Equivalently, \(A\subseteq A^*\): the domain \(\mathcal D(A)\) is contained in \(\mathcal D(A^*)\), and \(A^*x=Ax\) there, where \(A^*\) denotes the [[functional-analysis/adjoint-unbounded-operator|adjoint of a densely defined operator]]. Symmetry is thus an inclusion of domain-sensitive operators. It does not by itself give equality with the adjoint.

## Basic properties

Every symmetric operator is closable, and its closure is again symmetric. Its eigenvalues are real, and eigenvectors belonging to distinct eigenvalues are orthogonal. These facts resemble the bounded Hermitian theory, but the domain can obstruct both self-adjointness and the existence of a spectral resolution.

## Relationship to self-adjointness

A [[functional-analysis/self-adjoint-unbounded-operator|self-adjoint unbounded operator]] is symmetric, but a symmetric operator can have a strictly larger adjoint domain. [[functional-analysis/self-adjoint-extension|Self-adjoint extensions]] are controlled by the two deficiency subspaces \(\ker(A^*-iI)\) and \(\ker(A^*+iI)\); equal deficiency dimensions permit extensions, while both dimensions zero force self-adjointness [Schmüdgen, chapter 1 and part VI](https://doi.org/10.1007/978-94-007-4753-1).

## Example and warning

On \(L^2(0,1)\), the operator \(-i\,d/dx\) with domain \(C_c^\infty(0,1)\) is symmetric. Its adjoint has a larger Sobolev domain, so it is not self-adjoint.

**Warning.** In some physics usage “Hermitian” informally means self-adjoint. For unbounded operators, symmetric and self-adjoint must be kept distinct because boundary conditions determine the adjoint domain.

## References

1. Konrad Schmüdgen, *Unbounded Self-adjoint Operators on Hilbert Space*, Graduate Texts in Mathematics 265, Springer, 2012. [DOI record](https://doi.org/10.1007/978-94-007-4753-1). Relevant: chapter 1 and part VI on symmetric operators and self-adjoint extensions.
2. Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, revised edition, Academic Press, 1980. [Publisher record](https://www.sciencedirect.com/book/9780125850506/functional-analysis). Relevant: chapter VIII on unbounded operators.
