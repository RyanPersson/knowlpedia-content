+++
id = "functional-analysis/finite-rank-operator"
title = "Finite-rank operator"
kind = "definition"
summary = "A bounded linear operator whose range is finite-dimensional."
aliases = ["operator of finite rank"]
domains = ["functional-analysis"]
section_mode = "progressive"
+++

Let \(X\) and \(Y\) be
[[linear-algebra/normed-vector-space|normed vector spaces]] over the same
scalar field \(\mathbb R\) or \(\mathbb C\). A
[[functional-analysis/bounded-linear-operator|bounded linear operator]]
\(T:X\to Y\) is a **finite-rank operator** if its range \(T(X)\) is
finite-dimensional. Its **rank** is
\[
\operatorname{rank}T=\dim T(X).
\]
Thus the zero operator has rank \(0\), and \(T\) has rank \(n\) precisely
when its range has a
[[convex-analysis/basis-hamel-basis-and-dimension|Hamel basis]] of \(n\)
vectors. Boundedness is part of the operator-theoretic convention used here;
an algebraic [[linear-algebra/linear-map|linear map]] can have finite-dimensional range without being
continuous.

## Rank-one decompositions

An operator has finite rank exactly when it can be written
\[
Tx=\sum_{j=1}^{n}\varphi_j(x)y_j
\]
for finitely many continuous linear functionals \(\varphi_j\in X'\) and
vectors \(y_j\in Y\). Choosing the \(y_j\) as a basis for \(T(X)\) gives such
a representation, while every displayed sum has range contained in their
span. Rank-one operators \(x\mapsto\varphi(x)y\) are the elementary building
blocks [Conway, Chapter II].

## Approximation and examples

Finite-rank operators form a [[convex-analysis/linear-subspace|linear subspace]] of \(B(X,Y)\), are compact, and
are stable under composition with bounded operators. Their operator-norm
closure is the class of approximable operators; it need not contain every
[[linear-algebra/compact-operator|compact operator]] for arbitrary
[[linear-algebra/banach-space|Banach spaces]]. On
[[linear-algebra/hilbert-space|Hilbert spaces]], compact operators are
operator-norm limits of finite-rank operators, and finite-rank operators lie
in every
[[functional-analysis/schatten-class-operator|Schatten class]].

The identity on \(X\) is finite-rank exactly when \(X\) is finite-dimensional.
A nonzero functional \(\varphi\in X'\) and vector \(y\in Y\) give a rank-one
operator \(x\mapsto\varphi(x)y\).

## References

1. John B. Conway, *A Course in Functional Analysis*, 2nd ed., Graduate Texts in Mathematics 96, Springer, 1990. [Springer DOI record](https://doi.org/10.1007/978-1-4757-4383-8). Relevant: Chapter II, “Operators on Hilbert Space,” and the discussion of finite-rank and compact operators.
2. Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, revised and enlarged ed., Academic Press, 1980. [Elsevier book record](https://shop.elsevier.com/books/i-functional-analysis/reed/978-0-08-057048-8). Relevant: Chapter VI, “Bounded Operators.”
