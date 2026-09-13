+++
id = "linear-algebra/integer-lattice-index"
title = "Index of an integer sublattice"
kind = "theorem"
summary = "The quotient of the integer lattice by the image of a nonsingular integer matrix has order equal to its absolute determinant."
aliases = ["finite quotient of integer lattices", "determinant-index formula"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/euclidean-lattice", "linear-algebra/lattice-fundamental-domain", "linear-algebra/determinant", "algebra-groups/index-of-subgroup", "measure-theory/tonellis-theorem", "shared-foundations/rational-numbers"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

If \(A\) is a nonsingular \(n\times n\) integer matrix, then
\[
\bigl|\mathbb Z^n/A\mathbb Z^n\bigr|=|\det A|.
\]
The left side is the [[algebra-groups/index-of-subgroup|index]] of the sublattice \(A\mathbb Z^n\).

## Proof by fundamental domains

The entries of \(A^{-1}\) are rational. Choose a positive integer \(N\) clearing their denominators. Then \(N\mathbb Z^n\subset A\mathbb Z^n\), proving that the index \(k\) is finite. Take coset representatives \(r_1,\ldots,r_k\in\mathbb Z^n\). The union of \(r_j+[0,1)^n\) is a fundamental domain for \(A\mathbb Z^n\) of volume \(k\). The parallelepiped \(A[0,1)^n\) is another, of volume \(|\det A|\). Their volumes agree: partition one domain by its intersections with lattice translates of the other, translate the pieces back, and use countable additivity. This gives the formula.
