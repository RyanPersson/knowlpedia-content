+++
id = "real-analysis/tensor-field"
title = "Matrix-valued tensor field in Euclidean coordinates"
kind = "definition"
summary = "A field of matrices representing rank-two tensors in a chosen Euclidean basis."
aliases = ["tensor field", "matrix field", "matrix-valued field"]
domains = ["real-analysis"]
section_mode = "progressive"
prerequisites = ["linear-algebra/matrix", "shared-foundations/function", "linear-algebra/euclidean-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

In a fixed Euclidean basis, a **rank-two tensor field** is represented by a [[linear-algebra/matrix|matrix]]-valued map \(T:U\to\mathbb R^{n\times n}\). Here both tensor indices are identified using the Euclidean inner product. Under an orthogonal change of coordinates \(x'=Qx\), its components transform by
\[
T'(x')=QT(x)Q^T.
\]
This transformation rule distinguishes a tensor from an array of scalar fields with no specified geometric meaning.

## Momentum flux

For a vector field \(u\), the [[linear-algebra/outer-product|outer product]] \(u\otimes u\) has entries \(u_i u_j\). Its [[real-analysis/divergence-of-tensor|row divergence]] is the vector with components \(\sum_j\partial_j(u_i u_j)\). Stating which index is differentiated fixes the convention for nonsymmetric tensors.
