+++
id = "linear-algebra/eigenvector"
title = "Eigenvector"
kind = "knowl"
summary = "A nonzero vector that is scaled by a linear operator."
aliases = ["eigenvector"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/eigenvector.md"
prerequisites = ["linear-algebra/linear-operator"]
dependency_heuristic = "semantic-curriculum-review-v1"
dependency_review_count = 1
+++

An **eigenvector** of a [[linear-algebra/linear-operator|linear operator]] \(T:V\to V\) is a nonzero vector \(v\in V\) for which there exists a scalar \(\lambda\in\mathbb{F}\) such that
\[
T(v)=\lambda v.
\]
The corresponding scalar \(\lambda\) is an [[linear-algebra/eigenvalue|eigenvalue]] of \(T\).

## Remarks

The [[linear-algebra/eigenspace|eigenspace]] for an eigenvalue \(\lambda\) is \(\ker(T-\lambda I)\). Its nonzero vectors are precisely the eigenvectors with eigenvalue \(\lambda\); the zero vector belongs to the eigenspace but is not an eigenvector.

## Examples

- For \(A=\operatorname{diag}(2,3)\) on \(\mathbb{R}^2\), the vector \((1,0)\) is an eigenvector with eigenvalue \(2\).
- For the projection \(P(x,y)=(x,0)\), the vector \((1,0)\) is an eigenvector with eigenvalue \(1\) and \((0,1)\) is an eigenvector with eigenvalue \(0\).
- For the scaling map \(T(v)=c\,v\), every nonzero vector is an eigenvector with eigenvalue \(c\).
