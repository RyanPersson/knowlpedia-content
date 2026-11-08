+++
id = "algebra-rings/quaternion-fractional-ideal"
title = "Fractional ideal of a quaternion order"
kind = "definition"
summary = "A full lattice stable under left or right multiplication by a specified quaternion order."
aliases = ["fractional quaternion ideal", "right fractional quaternion ideal", "left fractional quaternion ideal"]
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-rings/quaternion-order", "algebra-modules/full-lattice"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

Let \(B\) be a [[algebra-rings/quaternion-algebra|quaternion algebra]] over a number field \(K\), let \(R=\mathcal O_K\), and let \(\mathcal O\subseteq B\) be an \(R\)-[[algebra-rings/quaternion-order|order]]. A **right fractional \(\mathcal O\)-ideal** is a [[algebra-modules/full-lattice|full \(R\)-lattice]] \(I\subseteq B\) with \(I\mathcal O\subseteq I\). A **left fractional ideal** instead satisfies \(\mathcal OI\subseteq I\).

The side is part of the definition. An ideal need not be contained in \(\mathcal O\); one contained in \(\mathcal O\) is called integral relative to that order.

## Principal ideals

For \(a\in B^\times\), the lattice \(a\mathcal O\) is a principal right fractional ideal, and \(\mathcal Oa\) is a principal left fractional ideal. They need not be the same subset.

Every fractional ideal has a denominator: some nonzero \(d\in R\) satisfies \(dI\subseteq\mathcal O\). This follows by expressing finitely many lattice generators in a fraction-field basis of the order.

## The fullness condition

In a split matrix algebra, a nonzero one-sided ideal in the ring-theoretic sense need not span the full algebra. For example, \(E_{11}M_2(R)\) has only its first row possibly nonzero and is not a full fractional ideal of \(M_2(R)\).

For ideal-class arithmetic one uses [[algebra-rings/locally-principal-quaternion-ideal|locally principal fractional ideals]]. This is different from the commutative definition of a fractional ideal inside a field.

## Products of one-sided ideals: a matrix example

For lattices \(I,J\subseteq B\), their product \(IJ\) means the additive subgroup consisting of finite sums of products \(xy\), with \(x\in I\) and \(y\in J\). This product exists even when their orders do not match. If both are right \(\mathcal O\)-ideals, then \((IJ)\mathcal O\subseteq IJ\); the problem is not this stability, but the loss of the usual identity and inverse laws.

Take the split quaternion algebra \(B=M_2(\mathbb Q)\), its [[algebra-rings/maximal-order|maximal order]] \(\mathcal O=M_2(\mathbb Z)\), and
\[
h=\begin{pmatrix}2&0\\0&1\end{pmatrix},
\qquad J=h\mathcal O
=\left\{\begin{pmatrix}2a&2b\\c&d\end{pmatrix}:a,b,c,d\in\mathbb Z\right\}.
\]
This is a full principal right ideal, proper because its first row is even. Let \(E_{ij}\) denote the matrix with entry \(1\) in position \((i,j)\) and zero elsewhere. Then
\[
E_{22}=E_{22}hE_{22},\qquad E_{11}=E_{12}hE_{21}.
\]
Both belong to the two-sided ideal \(\mathcal Oh\mathcal O=\mathcal OJ\). Their sum is \(1\), so
\[
\mathcal OJ=\mathcal O\ne J,
\qquad J\mathcal O=J.
\]
Thus \(\mathcal O\) is not a left identity for multiplication of arbitrary right ideals. Also \(E_{12}\in\mathcal OJ\setminus J\), so the inherited multiplication does not make \(J\) a left \(\mathcal O\)-module.

## Matching left and right orders

For a full lattice \(I\subset B\), write
\[
\mathcal O_L(I)=\{b\in B:bI\subseteq I\},
\qquad
\mathcal O_R(I)=\{b\in B:Ib\subseteq I\}.
\]
These are its left and right orders. In the example,
\[
\mathcal O_L(J)=h\mathcal Oh^{-1},\qquad \mathcal O_R(J)=\mathcal O.
\]
With \(J^{-1}=\mathcal Oh^{-1}\), direct multiplication gives
\[
JJ^{-1}=h\mathcal Oh^{-1},\qquad J^{-1}J=\mathcal O.
\]
Thus invertibility uses two different identity orders. A two-sided fractional \(\mathcal O\)-ideal is stable on both sides; for a maximal order its left and right orders both equal \(\mathcal O\).

The [[algebra-modules/tensor-product|tensor product]] \(I\otimes_{\mathcal O}J\) requires a right \(\mathcal O\)-action on \(I\) and a left \(\mathcal O\)-action on \(J\). Two right ideals alone do not supply this data. For compatible invertible ideals, with \(\mathcal O_R(I)=\mathcal O_L(J)\), the [[algebra-rings/ideal-tensor-multiplication-isomorphism|canonical multiplication map is an isomorphism]].

## References

1. John Voight, *Quaternion Algebras*, [author's text](https://jvoight.github.io/quat-book.pdf), Definition 16.2.9 and Remark 16.2.10.

2. John Voight, *Quaternion Algebras*, [Chapter 16](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_16), §16.2 and §16.3 (orders, compatible products, and inverses).
