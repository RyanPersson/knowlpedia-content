+++
id = "algebra-modules/jordan-canonical-form-theorem"
title = "Jordan canonical form theorem"
kind = "knowl"
summary = "Over a splitting field, every linear operator is similar to a direct sum of Jordan blocks."
aliases = ["jordan-canonical-form-theorem", "Jordan canonical form theorem"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/jordan-canonical-form-theorem.md"
prerequisites = ["linear-algebra/linear-map", "linear-algebra/vector-space", "linear-algebra/characteristic-polynomial", "linear-algebra/eigenvector"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(T\) be a linear operator on a finite-dimensional vector space \(V\) over a field \(k\). If the characteristic polynomial of \(T\) splits over \(k\), then \(V\) has a basis in which the matrix of \(T\) is block diagonal with Jordan blocks \(J_m(\lambda)\). The eigenvalues \(\lambda\) and, for each \(\lambda\), the multiset of block sizes are uniquely determined by \(T\), up to permuting the blocks.

## Consequences

Each block corresponds to a chain of generalized [[linear-algebra/eigenvector|eigenvectors]]. The operator \(T\) is [[algebra-modules/diagonalizable|diagonalizable]] exactly when every block has size \(1\), and the largest block size for \(\lambda\) is the exponent of \(x-\lambda\) in the [[linear-algebra/minimal-polynomial|minimal polynomial]].
