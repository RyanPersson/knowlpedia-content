+++
id = "nonassociative-algebra/peirce-decomposition"
title = "Peirce decomposition of a Jordan algebra"
kind = "construction"
summary = "The splitting of a Jordan algebra into the 0, one-half, and 1 eigenspaces of multiplication by an idempotent."
aliases = ["Jordan Peirce decomposition", "Peirce spaces", "Peirce eigenspaces"]
domains = ["nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["nonassociative-algebra/jordan-idempotent", "nonassociative-algebra/jordan-algebra", "nonassociative-algebra/jordan-subalgebra", "nonassociative-algebra/euclidean-jordan-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(e\) be an [[nonassociative-algebra/jordan-idempotent|idempotent]] in a
[[nonassociative-algebra/jordan-algebra|Jordan algebra]] \(J\) over a field of characteristic different from \(2\). Its
**Peirce spaces** are
\[
J_\lambda(e)=\{x\in J:e\circ x=\lambda x\},
\qquad \lambda\in\left\{0,\tfrac12,1\right\}.
\]
The Peirce decomposition theorem says that multiplication by \(e\) is
diagonalizable with these possible eigenvalues and gives the direct sum
\[
J=J_0(e)\oplus J_{1/2}(e)\oplus J_1(e).
\]

## Peirce multiplication rules

The Jordan product respects the decomposition through
\[
\begin{aligned}
J_1\circ J_1&\subseteq J_1,&
J_0\circ J_0&\subseteq J_0,&
J_1\circ J_0&=0,\\
(J_0+J_1)\circ J_{1/2}&\subseteq J_{1/2},&&
J_{1/2}\circ J_{1/2}&\subseteq J_0+J_1.
\end{aligned}
\]
Thus \(J_1(e)\) and \(J_0(e)\) are [[nonassociative-algebra/jordan-subalgebra|Jordan subalgebras]], while the middle space
mediates between them.

For a [[nonassociative-algebra/euclidean-jordan-algebra|Euclidean Jordan algebra]] the three summands are mutually orthogonal for
the [[nonassociative-algebra/trace-form-of-a-euclidean-jordan-algebra|trace
inner product]].

## Several frame idempotents

A [[nonassociative-algebra/jordan-frame|Jordan frame]] refines the
single-idempotent splitting into diagonal lines and pair spaces. This produces
the six-summand description of \(H_3(\mathbb K)\) in
[[nonassociative-algebra/frame-decomposition-of-hermitian-jordan-algebras|the
frame decomposition]].

## References

1. Nathan Jacobson, *Structure and Representations of Jordan Algebras*, American Mathematical Society, 1968, Chapter III, §1. [Publisher record](https://doi.org/10.1090/coll/039).
2. Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones*, Oxford University Press, 1994, Chapter IV, §1. [Publisher record](https://doi.org/10.1093/oso/9780198534778.001.0001).
