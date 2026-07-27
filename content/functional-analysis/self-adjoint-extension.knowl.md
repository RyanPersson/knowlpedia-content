+++
id = "functional-analysis/self-adjoint-extension"
title = "Self-adjoint extension"
kind = "definition"
summary = "A self-adjoint operator that extends a given symmetric operator without changing its action on the original domain."
aliases = ["self-adjoint operator extension"]
domains = ["functional-analysis"]
section_mode = "progressive"
+++

Let \(A:\mathcal D(A)\subseteq H\to H\) be a densely defined
[[functional-analysis/symmetric-operator|symmetric operator]] on a complex
[[linear-algebra/hilbert-space|Hilbert space]]. A **self-adjoint extension** of \(A\) is a
[[functional-analysis/self-adjoint-unbounded-operator|self-adjoint operator]]
\(\widetilde A\) on \(H\) such that \(A\subseteq\widetilde A\): explicitly,
\[
\mathcal D(A)\subseteq\mathcal D(\widetilde A)
\quad\text{and}\quad
\widetilde A x=Ax\ \text{for every }x\in\mathcal D(A).
\]
The domain enlargement is part of the construction. A self-adjoint operator
with the same formal differential expression but incompatible boundary values
is not an extension in this operator-theoretic sense.

## Von Neumann parametrization

Assume \(A\) is closed and let
\(\mathcal N_\pm=\ker(A^*\mp iI)\). Self-adjoint extensions exist exactly when
the [[functional-analysis/deficiency-indices|deficiency indices]] are equal.
Each unitary map \(U:\mathcal N_+\to\mathcal N_-\) determines one by
\[
\mathcal D(A_U)
=\mathcal D(A)\mathbin{\dotplus}
\{u+Uu:u\in\mathcal N_+\},
\]
\[
A_U(x+u+Uu)=Ax+iu-iUu.
\]
Every self-adjoint extension arises uniquely in this way
[Schmüdgen, Chapter 13](https://doi.org/10.1007/978-94-007-4753-1).

## Boundary conditions

For differential operators, the deficiency data are often encoded by boundary
values. The minimal operator \(-i\,d/dx\) on an interval has self-adjoint
extensions with domains satisfying
\[
f(1)=e^{i\theta}f(0),\qquad \theta\in[0,2\pi).
\]
The minimal Laplacian on an interval likewise has many extensions, including
Dirichlet, Neumann, and periodic realizations. These choices can have different
spectra even though they agree with the same differential expression on
[[functional-analysis/test-function-space|compactly supported smooth functions]].

## Uniqueness and nonexistence

If both deficiency indices vanish, \(A\) is
[[functional-analysis/essentially-self-adjoint-operator|essentially
self-adjoint]] and its closure is its unique self-adjoint extension. Equal
positive indices yield multiple extensions; unequal indices yield none on the
given Hilbert space. Thus symmetry alone neither guarantees existence nor
uniqueness. Additional structure, such as lower semiboundedness, may select a
canonical extension without making it the only one.

## References

1. Konrad Schmüdgen, *Unbounded Self-adjoint Operators on Hilbert Space*, Graduate Texts in Mathematics 265, Springer, 2012. [DOI record](https://doi.org/10.1007/978-94-007-4753-1). Relevant: Chapter 13 on von Neumann’s extension theory.
2. Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics II: Fourier Analysis, Self-Adjointness*, Academic Press, 1975. [Bibliographic record](https://catalogue.bnf.fr/ark:/12148/cb37359774j). Relevant: Chapter X on self-adjoint extensions and boundary conditions.
