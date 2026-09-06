+++
id = "nonassociative-algebra/euclidean-jordan-algebra"
title = "Euclidean Jordan algebra"
kind = "definition"
summary = "A finite-dimensional real Jordan algebra with a positive-definite inner product associative with the Jordan product."
aliases = ["Euclidean Jordan algebra", "EJA", "formally real Jordan algebra"]
domains = ["nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["nonassociative-algebra/jordan-algebra", "linear-algebra/inner-product"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **Euclidean Jordan algebra** is a finite-dimensional real unital
[[nonassociative-algebra/jordan-algebra|Jordan algebra]] \(J\), together with a
positive-definite [[linear-algebra/inner-product|inner product]]
\(\langle-,-\rangle\), such that
\[
\langle x\circ y,z\rangle=\langle y,x\circ z\rangle
\qquad(x,y,z\in J).
\]
Equivalently, every multiplication operator \(L_x(y)=x\circ y\) is
self-adjoint.

## Euclidean versus formally real

A real Jordan algebra is **formally real** if
\[
x_1^2+\cdots+x_m^2=0
\quad\Longrightarrow\quad
x_1=\cdots=x_m=0.
\]
Formal reality is a property of the algebra; a Euclidean structure includes a
chosen compatible inner product. In finite dimensions, a real unital Jordan
algebra is formally real exactly when it admits such a Euclidean inner
product. The terms are therefore often used interchangeably when classifying
algebras, but they are not literally identical data.

## Spectral theorem

Every \(x\in J\) admits a spectral decomposition
\[
x=\lambda_1c_1+\cdots+\lambda_rc_r,
\]
where the \(c_i\) are pairwise orthogonal primitive idempotents summing to the
unit. A maximal such family is a [[nonassociative-algebra/jordan-frame|Jordan frame]], and its cardinality is the
rank. This gives a functional calculus, the Jordan trace
\(\operatorname{tr}_J(x)=\sum_i\lambda_i\), and the determinant
\(\det_J(x)=\prod_i\lambda_i\).

## Cone of squares

The cone
\[
J_+=\{x^2:x\in J\}
\]
is closed, convex, and self-dual, and its interior is homogeneous. Conversely,
every homogeneous self-dual open cone arises from a Euclidean Jordan algebra.
This is the bridge between Jordan theory and symmetric cones.

## Classification

Every Euclidean Jordan algebra is an orthogonal direct sum of
[[nonassociative-algebra/simple-euclidean-jordan-algebra|simple Euclidean
Jordan algebras]]. The simple factors are the real, complex, and quaternionic
Hermitian matrix families, [[nonassociative-algebra/spin-factor-jordan-algebra|spin factors]], and
\(\mathfrak h_3(\mathbb O)\).

## References

1. Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones*, Oxford University Press, 1994. [Publisher record](https://global.oup.com/academic/product/analysis-on-symmetric-cones-9780198534778).
2. Pascual Jordan, John von Neumann, and Eugene Wigner, “On an Algebraic Generalization of the Quantum Mechanical Formalism,” *Annals of Mathematics* 35 (1934), 29–64. [JSTOR record](https://www.jstor.org/stable/1968117).
