+++
id = "linear-algebra/matrix-inverse"
title = "Inverse matrix"
kind = "definition"
summary = "A square matrix whose product with a given matrix on either side is the identity."
aliases = ["matrix inverse", "invertible matrix", "two-sided inverse matrix"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/matrix", "linear-algebra/linear-map", "shared-foundations/inverse-function", "linear-algebra/determinant"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For a square [[linear-algebra/matrix|matrix]] \(A\) over a field, an **inverse matrix** is a matrix \(A^{-1}\) satisfying
\[
A^{-1}A=I=AA^{-1}.
\]
It exists exactly when the represented [[linear-algebra/linear-map|linear map]] is [[shared-foundations/bijective-function|bijective]], equivalently when \(\det A\ne0\). It is unique: if \(B A=I=A C\), then \(B=B(AC)=(BA)C=C\).

## Products and parameters

If \(A,B\) are invertible then \((AB)^{-1}=B^{-1}A^{-1}\). For a differentiable family of invertible matrices,
\[
\frac{d}{dt}A(t)^{-1}=-A(t)^{-1}A'(t)A(t)^{-1}.
\]
This follows by differentiating \(A^{-1}A=I\). Entrywise smoothness of the inverse also follows from the adjugate formula on the open set where the determinant is nonzero; uniform inverse bounds require quantitative control away from singular matrices.

## References

- [Sheldon Axler, Linear Algebra Done Right, 4th ed., Chapters 2–3, 6 and 9](https://linear.axler.net/LADR4e.pdf).
