+++
id = "linear-algebra/vandermonde-matrix"
title = "Vandermonde matrix"
kind = "definition"
summary = "The matrix of consecutive nonnegative integer powers of a list of nodes."
aliases = ["Vandermonde determinant"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/matrix", "linear-algebra/determinant", "real-analysis/polynomial"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For scalars \(x_1,\ldots,x_m\), the **Vandermonde matrix** is
\[
V_{ij}=x_j^{i-1},\qquad 1\le i,j\le m.
\]
Its [[linear-algebra/determinant|determinant]] is \(\prod_{1\le j<k\le m}(x_k-x_j)\), so it is invertible precisely when the nodes are distinct.

## Determinant argument

The determinant is an alternating polynomial in the nodes, hence divisible by every difference \(x_k-x_j\). Its total degree equals that of their product, so the quotient is constant. Comparing the coefficient of \(x_2x_3^2\cdots x_m^{m-1}\) gives constant one. Transposing the matrix changes the row-column convention but preserves the determinant.
