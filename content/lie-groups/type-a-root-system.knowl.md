+++
id = "lie-groups/type-a-root-system"
title = "Type A root system"
kind = "definition"
summary = "The simply laced root system A_n formed by the differences e_i-e_j in the sum-zero hyperplane of R^{n+1}."
aliases = ["type A root system", "A_n root system", "root system of type A"]
domains = ["lie-groups"]
section_mode = "progressive"
prerequisites = ["linear-algebra/euclidean-space", "lie-groups/simply-laced-root-system"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

For \(n\geq1\), the **root system of type \(A_n\)** is
\[
A_n=\{e_i-e_j:1\leq i\neq j\leq n+1\}
\]
in the \(n\)-dimensional [[linear-algebra/euclidean-space|Euclidean space]]
\[
V=\left\{(x_1,\ldots,x_{n+1})\in\mathbb R^{n+1}:\sum_i x_i=0\right\}.
\]
It is an irreducible [[lie-groups/simply-laced-root-system|simply laced root system]] of rank \(n\).

## Simple roots and diagram

A standard base of [[lie-groups/simple-root|simple roots]] is
\[
\alpha_i=e_i-e_{i+1},\qquad 1\leq i\leq n.
\]
Its [[lie-groups/dynkin-diagram|Dynkin diagram]] is a chain of \(n\) vertices. The system has \(n(n+1)\) roots, and its [[lie-groups/weyl-group|Weyl group]] is the symmetric group \(S_{n+1}\), acting by permuting coordinates.

## Lie-algebra realization

The roots of \(\mathfrak{sl}_{n+1}(\mathbb C)\) relative to its diagonal trace-zero [[lie-groups/cartan-subalgebra|Cartan subalgebra]] are the functionals \(e_i-e_j\). Hence type \(A_n\) corresponds under the [[lie-groups/classification-simple-lie-algebras|classification of complex simple Lie algebras]] to
\[
\mathfrak{sl}_{n+1}(\mathbb C),
\]
whose dimension is \((n+1)^2-1=n(n+2)\). See also the [[lie-groups/special-linear-lie-algebra|special linear Lie algebra]].

## Low-rank cases

The system \(A_1\) consists of two opposite roots. The accidental diagram isomorphism \(A_3\cong D_3\) is why the irreducible type \(D_n\) family is conventionally indexed from \(n=4\).

## References

1. James E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Springer, 1972, §§11–12. [Publisher record](https://doi.org/10.1007/978-1-4612-6398-2).
2. Nicolas Bourbaki, *Lie Groups and Lie Algebras, Chapters 4–6*, Springer, 2002, Chapter VI, §4. [Publisher record](https://link.springer.com/book/9783540691716).
3. John C. Baez, “Three Generations in \(E_7\),” 2026, §§2, 5, 7–8. [arXiv record](https://arxiv.org/abs/2608.06271).
