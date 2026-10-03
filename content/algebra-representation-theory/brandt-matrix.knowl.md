+++
id = "algebra-representation-theory/brandt-matrix"
title = "Brandt matrix"
kind = "definition"
summary = "An integer matrix counting quaternion ideal neighbors according to ideal class."
aliases = ["Brandt matrices", "n-Brandt matrix"]
domains = ["algebra-representation-theory"]
section_mode = "progressive"
prerequisites = ["algebra-rings/quaternion-ideal-class-set", "algebra-rings/quaternion-fractional-ideal", "algebra-rings/maximal-order", "algebra-rings/quaternion-algebra", "algebra-rings/locally-principal-quaternion-ideal"]
dependency_heuristic = "transcript-connections-semantic-v1"
dependency_review_count = 1
+++
Let \(\mathcal O\) be a [[algebra-rings/maximal-order|maximal order]] in a definite [[algebra-rings/quaternion-algebra|quaternion algebra]] over \(\mathbb Q\), and choose representatives \(I_1,\ldots,I_h\) of its right [[algebra-rings/quaternion-ideal-class-set|ideal classes]]. For \(n\ge1\), its **Brandt matrix** is
\[
T(n)_{ij}
=\#\{J\subseteq I_j:[I_j:J]=n^2,\ [J]=[I_i]\},
\]
where \(J\) ranges over [[algebra-rings/locally-principal-quaternion-ideal|locally principal]] right [[algebra-rings/quaternion-fractional-ideal|\(\mathcal O\)-ideals]]. The index is that of additive lattices, and \([J]=[I_i]\) means \(J=\alpha I_i\) for some invertible quaternion \(\alpha\). Column \(j\) records the classes of the subideals of \(I_j\).

## Prime neighbors

If \(\ell\) is prime and does not divide the quaternion discriminant, every column of \(T(\ell)\) sums to \(\ell+1\). It describes a directed multigraph on the ideal classes: the entry counts arrows from the column class to the row class, so multiple arrows are allowed. The matrix need not be symmetric in this basis.

## Modular interpretation

These counts can also be expressed through representation numbers of positive definite quadratic lattices. Their [[linear-algebra/theta-series-of-lattice|theta series]] connect quaternion ideal arithmetic with weight-two [[complex-analysis/modular-form|modular forms]]. Transposing the convention exchanges row and column descriptions without changing the underlying correspondence.

## References

1. John Voight, *Quaternion Algebras*, [§41.1](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_41), equation (41.1.1), the following prime column-sum statement, and §§41.1.3–41.1.9.
