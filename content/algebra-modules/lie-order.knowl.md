+++
id = "algebra-modules/lie-order"
title = "Lie order"
kind = "definition"
summary = "A full integral lattice in a finite-dimensional Lie algebra that is closed under the bracket."
aliases = ["Lie order", "Lie lattice", "Lie Z-order", "integral Lie form"]
domains = ["algebra-modules"]
section_mode = "progressive"
prerequisites = ["lie-groups/lie-algebra", "algebra-modules/full-lattice", "algebra-commutative/noetherian-ring"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

Let \(R\) be a [[algebra-commutative/noetherian-ring|Noetherian]] integral domain with [[algebra-rings/fraction-field|fraction field]] \(K\), and let \(\mathfrak g\) be a finite-dimensional \(K\)-[[lie-groups/lie-algebra|Lie algebra]]. A **Lie \(R\)-order** in \(\mathfrak g\) is a [[algebra-modules/full-lattice|full \(R\)-lattice]] \(L\subseteq\mathfrak g\) satisfying \([L,L]\subseteq L\).

Thus the Lie bracket restricts to \(L\), and \(K\otimes_R L\cong\mathfrak g\) as Lie algebras. Such an \(L\) is also called an integral Lie form or Lie lattice; the word “order” here refers to the Lie operation.

## The rank-three example

For \(K=\mathbb Q\), put
\[
e=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
f=\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad
h=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
Then \(\mathfrak{sl}_2(\mathbb Z)=\mathbb Ze\oplus\mathbb Zh\oplus\mathbb Zf\) is a Lie order because
\[
[h,e]=2e,\qquad[h,f]=-2f,\qquad[e,f]=h.
\]
This is the basic [[lie-groups/chevalley-basis|Chevalley basis]] example.

## Changing the base ring

The same basis gives a Lie \(\mathbb Z[i]\)-order \(\mathfrak{sl}_2(\mathbb Z[i])\) in \(\mathfrak{sl}_2(\mathbb Q(i))\). Under [[algebra-commutative/restriction-of-scalars|restriction of scalars]] it is also a rank-six Lie \(\mathbb Z\)-order, with basis \(e,ie,h,ih,f,if\).

Neither trace-zero lattice is an [[algebra-rings/order-in-algebra|associative order]] under matrix multiplication: \(ef=\operatorname{diag}(1,0)\) is not trace zero. The corresponding associative examples are the full [[algebra-rings/matrix-ring|matrix rings]].

## References

1. The displayed matrix products directly verify bracket closure and failure of associative closure.
2. For the general semisimple construction and its literature, see [[lie-groups/chevalley-basis|Chevalley basis]] and [[algebraic-geometry-foundations/chevalley-lattice-integral-model|Chevalley lattice and integral model]].
