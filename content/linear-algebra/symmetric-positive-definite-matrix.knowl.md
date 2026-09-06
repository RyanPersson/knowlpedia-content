+++
id = "linear-algebra/symmetric-positive-definite-matrix"
title = "Symmetric positive-definite matrix"
kind = "definition"
summary = "A real symmetric matrix whose quadratic form is strictly positive on every nonzero vector."
aliases = ["positive-definite symmetric matrix", "SPD matrix", "Sym++(n,R)", "positive-definite cone"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/matrix"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A real \(n\times n\) matrix \(A\) is **symmetric positive definite** if
\(A^T=A\) and

\[
v^TAv>0
\]

for every nonzero \(v\in\mathbb R^n\). The set of such matrices is often
denoted \(\operatorname{Sym}_{++}(n,\mathbb R)\).

## Equivalent characterizations

For a real symmetric matrix, positive definiteness is equivalent to all
eigenvalues being positive. It is also equivalent to the existence of an
invertible matrix \(B\) with \(A=B^TB\), and to positivity of all leading
principal minors.

## Geometry of the cone

The symmetric positive-definite matrices form an open convex cone in the
vector space of real symmetric matrices. A Riemannian metric in local
coordinates is a smoothly varying matrix with values in this cone.

## References

1. Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed., Cambridge University Press, 2012. [Publisher record](https://doi.org/10.1017/CBO9781139020411). Relevant: positive-definite matrices.
