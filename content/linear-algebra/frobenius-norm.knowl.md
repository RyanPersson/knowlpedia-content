+++
id = "linear-algebra/frobenius-norm"
title = "Frobenius norm"
kind = "definition"
summary = "The Euclidean norm of the list of entries of a finite matrix."
aliases = ["Hilbert–Schmidt matrix norm"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/matrix", "linear-algebra/euclidean-norm", "shared-foundations/finite-sum", "shared-foundations/complex-numbers-c", "shared-foundations/complex-conjugate"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

For a real or complex finite matrix \(A=(a_{ij})\), its **Frobenius norm** is
\[
\|A\|_F=\left(\sum_{i,j}|a_{ij}|^2\right)^{1/2}.
\]
It is the [[linear-algebra/euclidean-norm|Euclidean norm]] of its entries, with complex absolute values in the complex case.

## Gradient convention

For a vector field, \(|\nabla u|^2=\sum_{i,j}|\partial_j u_i|^2\) uses this norm on the Jacobian matrix. It differs from the operator norm, although all matrix norms on a fixed finite-dimensional matrix space are equivalent.
