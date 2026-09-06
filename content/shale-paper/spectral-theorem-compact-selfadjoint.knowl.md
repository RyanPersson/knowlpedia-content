+++
id = "shale-paper/spectral-theorem-compact-selfadjoint"
title = "Spectral Theorem for Compact Selfadjoint Operators"
kind = "knowl"
summary = "A compact self-adjoint operator on a separable Hilbert space has an orthonormal eigenbasis, with nonzero eigenvalues tending to zero."
aliases = ["spectral-theorem-compact-selfadjoint", "Spectral Theorem for Compact Selfadjoint Operators"]
domains = ["shale-paper"]
prerequisites = ["linear-algebra/hilbert-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
legacy_source_path = "shale-paper/spectral-theorem-compact-selfadjoint.md"
+++

Let \(A\) be a compact self-adjoint operator on a separable Hilbert space \(H\). Then \(H\) has an orthonormal basis of eigenvectors of \(A\). Every eigenvalue is real, each nonzero eigenvalue has finite multiplicity, and the nonzero eigenvalues form a finite sequence or a sequence tending to \(0\). The kernel of \(A\) is the zero-eigenspace and may be infinite-dimensional.

## Remarks

### Use in the paper
- Applied to positive [[shale-paper/hilbert-schmidt-operator|Hilbert–Schmidt]] operators to compute products like
\(\prod_k (2\lambda_k/(\lambda_k^2+1))^{1/2}\) (Lemma 3.2).
- Ensures existence of "eigensystems" used in continuity arguments (Lemma 2.4).

## Examples

- A diagonal operator on \(\ell^2\) with diagonal entries \(\lambda_k\to0\).
