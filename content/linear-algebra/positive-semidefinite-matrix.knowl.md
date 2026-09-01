+++
id = "linear-algebra/positive-semidefinite-matrix"
title = "Positive semidefinite matrix"
kind = "definition"
summary = "A real symmetric or complex Hermitian matrix whose quadratic form is nonnegative."
aliases = ["nonnegative definite matrix", "PSD matrix", "positive semidefinite Hermitian matrix", "positive matrix in Loewner order"]
domains = ["linear-algebra", "functional-analysis"]
prerequisites = ["linear-algebra/matrix", "linear-algebra/inner-product-space"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(A\in M_n(\mathbb F)\), where
\(\mathbb F=\mathbb R\) or \(\mathbb C\). The
[[linear-algebra/matrix|matrix]] \(A\) is **positive semidefinite**, written
\(A\succeq0\) or \(A\geq0\), if \(A=A^*\) and
\[
x^*Ax\geq0\qquad\text{for every }x\in\mathbb F^n.
\]
Here \(A^*\) is the transpose in the real case and the conjugate transpose in
the complex case. It is **positive definite** if
\(x^*Ax>0\) for every nonzero \(x\). Semidefiniteness permits a nontrivial
kernel; definiteness does not. The condition is basis-independent when \(A\)
is regarded as the matrix of a self-adjoint operator on a finite-dimensional
[[linear-algebra/inner-product-space|inner-product space]].

## Equivalent characterizations

For a Hermitian matrix \(A\), the following are equivalent:

- \(A\) is positive semidefinite;
- every [[linear-algebra/eigenvalue|eigenvalue]] of \(A\) is nonnegative;
- there is a matrix \(B\) such that \(A=B^*B\);
- \(A\) has a unique positive semidefinite square root \(A^{1/2}\).

The factorization can be obtained from the spectral theorem. It also
identifies positive semidefinite matrices with Gram matrices:
\(A_{ij}=\langle v_j,v_i\rangle\) for some finite family of vectors, subject
to the convention chosen for which inner-product variable is linear.

## Cone and order

Positive semidefinite matrices form a closed convex cone: if
\(A,B\succeq0\) and \(s,t\geq0\), then \(sA+tB\succeq0\). The
**Loewner order** on Hermitian matrices is
\[
A\preceq B\quad\Longleftrightarrow\quad B-A\succeq0.
\]
This is a [[shared-foundations/partial-order|partial order]], but it is not a total order when \(n>1\). Congruence
preserves positivity: \(A\succeq0\) implies \(C^*AC\succeq0\) for every
compatible matrix \(C\).

## Tests and examples

Every matrix \(B^*B\) is positive semidefinite. Covariance and Gram matrices
are standard examples. A diagonal Hermitian matrix is positive semidefinite
exactly when all diagonal entries are nonnegative.

Nonnegative entries do not imply positive semidefiniteness, and positive
semidefinite matrices may have negative off-diagonal entries. Sylvester's
criterion using strictly positive leading principal minors characterizes
positive definiteness; for semidefiniteness one instead requires all
principal minors to be nonnegative.

## References

1. Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed., Cambridge University Press, 2013. [DOI record](https://doi.org/10.1017/CBO9781139020411). Relevant: Chapters 4 and 7 on Hermitian matrices, quadratic forms, and positive semidefinite matrices.
2. Rajendra Bhatia, *Positive Definite Matrices*, Princeton University Press, 2007. [DOI record](https://doi.org/10.1515/9781400827787). Relevant: Chapter 1 on positivity, factorization, and the Loewner order.
