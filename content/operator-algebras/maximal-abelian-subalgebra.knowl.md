+++
id = "operator-algebras/maximal-abelian-subalgebra"
title = "Maximal abelian von Neumann subalgebra"
kind = "definition"
summary = "An abelian von Neumann subalgebra equal to its relative commutant."
aliases = ["MASA", "maximal abelian subalgebra"]
domains = ["operator-algebras"]
section_mode = "progressive"
prerequisites = ["operator-algebras/von-neumann-algebra", "operator-algebras/commutant"]
+++

A unital abelian [[operator-algebras/von-neumann-algebra|von Neumann subalgebra]] \(A\subseteq M\) is **maximal abelian** if no strictly larger abelian von Neumann subalgebra of \(M\) contains it. Equivalently,
\[
A'\cap M=A.
\]
It is often called a **MASA**.

## Example and use

Diagonal matrices form a MASA in \(M_n(\mathbb C)\). For an essentially free action of a countable group on a standard probability space, the function algebra \(L^\infty(X)\) is a MASA in the group–measure-space crossed product. This forces every central element to belong to the function algebra.

## References

1. Sorin Popa, [*Ergodic theory of group actions*](https://www.math.ucla.edu/~popa/Books/OElectures.pdf). Theorem 4.1.1 and §4.3.
