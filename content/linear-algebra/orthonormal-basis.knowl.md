+++
id = "linear-algebra/orthonormal-basis"
title = "Orthonormal basis"
kind = "knowl"
summary = "A basis whose vectors have unit length and are pairwise orthogonal."
aliases = ["orthonormal basis", "orthonormal bases"]
domains = ["linear-algebra", "quantum-foundations"]
prerequisites = ["linear-algebra/hilbert-space", "topology/closure", "convex-analysis/subspace-generated-by-a-set-span"]
dependency_heuristic = "axiomatic-dependency-review-v1"
dependency_review_count = 2
+++

An **orthonormal basis** of a [[linear-algebra/hilbert-space|Hilbert space]] \(H\) is a family \((e_i)_{i\in I}\) whose [[topology/closure|closed]] [[convex-analysis/subspace-generated-by-a-set-span|linear span]] is \(H\) and which satisfies
\[
\langle e_i,e_j\rangle=\delta_{ij}.
\]
## Interpretation

Thus each basis vector has norm one, distinct basis vectors are orthogonal, and every vector in \(H\) can be approximated in norm by finite linear combinations of the \(e_i\). In finite dimensions, “closed linear span” may be replaced by “linear span.”

## Expansion

Every \(x\in H\) has the norm-convergent expansion
\[
x=\sum_{i\in I}\langle x,e_i\rangle e_i.
\]
The coefficient order uses the convention that the inner product is linear in its first argument. For arbitrary index sets, the sum means the norm limit over finite subsets; each vector has at most countably many nonzero coefficients.

In a finite-dimensional complex space, placing the basis vectors as columns gives a unitary matrix.
