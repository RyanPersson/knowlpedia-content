+++
id = "algebra-rings/order-in-algebra"
title = "Order in an algebra"
kind = "definition"
summary = "An R-order is a unital subring that is a full R-lattice in a finite-dimensional fraction-field algebra."
aliases = ["R-order", "Z-order", "order in an algebra", "integral order"]
domains = ["algebra-rings"]
section_mode = "progressive"
prerequisites = ["algebra-modules/algebra-over-ring", "algebra-modules/full-lattice", "algebra-commutative/noetherian-ring"]
dependency_heuristic = "semantic-transcript-review-v1"
dependency_review_count = 1
+++

Let \(R\) be a [[algebra-commutative/noetherian-ring|Noetherian]] integral domain with [[algebra-rings/fraction-field|fraction field]] \(K\), and let \(A\ne0\) be a finite-dimensional associative unital \(K\)-[[algebra-modules/algebra-over-ring|algebra]]. An **\(R\)-order** in \(A\) is a subring \(\mathcal O\subseteq A\) containing \(1_A\) that is a [[algebra-modules/full-lattice|full \(R\)-lattice]]: \(\mathcal O\) is a finitely generated \(R\)-submodule and \(K\mathcal O=A\).

The scalar action is inherited from \(A\); in particular \(R1_A\subseteq\mathcal O\). The algebra and its order may be noncommutative.

## Z-orders

A **\(\mathbb Z\)-order** is this construction with \(R=\mathbb Z\) and \(K=\mathbb Q\). Its additive group is free of rank \(\dim_{\mathbb Q}A\).

Examples are \(M_n(\mathbb Z)\subset M_n(\mathbb Q)\) and, for a finite group \(G\), the [[algebra-representation-theory/group-algebra|group ring]] \(\mathbb Z[G]\subset\mathbb Q[G]\). The matrix units and group elements respectively give the required bases.

## Number fields and quaternion algebras

In a [[algebra-fields-galois/number-field|number field]] \(K\), every \(\mathbb Z\)-order lies with finite additive index in the [[algebra-fields-galois/ring-of-integers|ring of integers]] \(\mathcal O_K\). Indeed, multiplication by any element of the order has an integral matrix on its lattice, so its [[linear-algebra/characteristic-polynomial|characteristic polynomial]] proves integrality.

In \(\mathbb Q(i)\), the rings \(\mathbb Z+f\mathbb Zi\), \(f\ge1\), are orders of index \(f\) in \(\mathbb Z[i]\). Noncommutative examples include [[algebra-rings/quaternion-order|quaternion orders]].

## Conventions

Finite generation does not imply freeness over a general [[algebra-commutative/dedekind-domain|Dedekind domain]]. We use associative multiplication here; a bracket-closed integral form of a Lie algebra is a [[algebra-modules/lie-order|Lie order]].

## References

1. John Voight, *Quaternion Algebras*, [author's text](https://jvoight.github.io/quat-book.pdf), Definition 10.2.1 and Examples 10.2.3–10.2.4.
2. Andrew Sutherland, [MIT 18.785 Lecture 7](https://math.mit.edu/classes/18.785/2015fa/LectureNotes7.pdf), Remark 7.4.
