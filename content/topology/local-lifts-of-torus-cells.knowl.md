+++
id = "topology/local-lifts-of-torus-cells"
title = "Local lifts of cells under a torus covering"
kind = "definition"
summary = "A sufficiently small cell has finitely many disjoint lifted copies, labeled by an integer-lattice quotient."
aliases = ["lifted auxiliary rectangle", "torus cell lift"]
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["topology/integer-matrix-torus-cover", "linear-algebra/lattice-fundamental-domain", "shared-foundations/quotient-set", "shared-foundations/cartesian-product", "linear-algebra/matrix-inverse"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(p_A\) be an [[topology/integer-matrix-torus-cover|integer torus covering]], and let the connected cell \(C\subset\mathbb T^n\) lie in a sufficiently small evenly covered coordinate neighborhood. Choose a Euclidean lift \(\widetilde C\). The components of \(p_A^{-1}(C)\) have the form
\[
\bigl[A^{-1}(\widetilde C+k)\bigr],
\qquad k\in\mathbb Z^n/A\mathbb Z^n.
\]
Thus there are \(|\det A|\) lifted copies. Quotient representatives give sheet labels, not extra continuous variables.

## Rectangular coordinates

If \(\widetilde C=c+B\prod_j(-r_j,r_j)\), with \(B\) invertible, the local coordinate is \(\xi=B^{-1}(Y-c-k)\). The directional derivative along column \(j\) of \(B\) is \(\partial_{\xi_j}\). Smooth compactly supported functions in the cell can be extended by zero outside it. The center, covering matrix, and sheet representative are held fixed during these local differentiations.
