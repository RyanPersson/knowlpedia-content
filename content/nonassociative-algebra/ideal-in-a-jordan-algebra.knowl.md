+++
id = "nonassociative-algebra/ideal-in-a-jordan-algebra"
title = "Ideal in a Jordan algebra"
kind = "definition"
summary = "A linear subspace stable under multiplication by every element of the ambient Jordan algebra."
aliases = ["Jordan ideal", "ideal of a Jordan algebra", "Jordan algebra ideal"]
domains = ["nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["nonassociative-algebra/jordan-algebra", "convex-analysis/linear-subspace", "linear-algebra/vector-space", "nonassociative-algebra/jordan-algebra-homomorphism", "nonassociative-algebra/jordan-subalgebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(J\) be a [[nonassociative-algebra/jordan-algebra|Jordan algebra]]. An
**ideal** of \(J\) is a [[convex-analysis/linear-subspace|linear subspace]] \(I\subseteq J\) such that

\[
x\circ y\in I
\qquad\text{for every }x\in J\text{ and }y\in I.
\]

Equivalently, every multiplication operator \(L_x:y\mapsto x\circ y\)
preserves \(I\). Because the Jordan product is commutative, no separate left-
and right-ideal conditions are needed.

## Quotients and kernels

The quotient [[linear-algebra/vector-space|vector space]] \(J/I\) has the well-defined Jordan product

\[
(x+I)\circ(y+I)=x\circ y+I.
\]

The quotient map \(J\to J/I\) is a
[[nonassociative-algebra/jordan-algebra-homomorphism|Jordan homomorphism]].
Conversely, the kernel of every Jordan homomorphism is an ideal. These facts
make ideals the subobjects appropriate to quotient constructions; an arbitrary
[[nonassociative-algebra/jordan-subalgebra|Jordan subalgebra]] need not be an
ideal.

## Units and simplicity

If \(J\) has unit \(1\) and an ideal \(I\) contains \(1\), then
\(x=x\circ1\in I\) for every \(x\in J\), so \(I=J\). A nonzero Jordan algebra
is **simple** when it has no ideals other than \(0\) and \(J\), together with
the usual convention excluding the one-dimensional zero-product degeneracy.

When \(J\) is a direct sum of ideals, multiplication between distinct summands
vanishes. In particular, the simple-factor decomposition of a Euclidean
Jordan algebra is a decomposition by ideals, not merely by subalgebras.

## Warning about quadratic Jordan theory

This definition uses the bilinear Jordan-algebra convention in characteristic
different from \(2\). Over more general base rings, quadratic Jordan algebras
use a stronger ideal condition involving their quadratic operators; that
notion should not be silently identified with the one used here.

## References

1. Nathan Jacobson, *Structure and Representations of Jordan Algebras*,
   American Mathematical Society, 1968, Chapters I and V. [Publisher record](https://doi.org/10.1090/coll/039).
2. Kevin McCrimmon, *A Taste of Jordan Algebras*, Springer, 2004, §§1.5 and
   4.2. [Publisher record](https://doi.org/10.1007/b97489).
