+++
id = "linear-algebra/signature-of-symmetric-bilinear-form"
title = "Signature of a symmetric bilinear form"
kind = "definition"
summary = "The numbers of negative and positive squares in a real symmetric bilinear form."
aliases = ["inertia of a real symmetric bilinear form", "signature of a quadratic form"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/bilinear-form", "linear-algebra/vector-space", "linear-algebra/quadratic-form", "convex-analysis/basis-hamel-basis-and-dimension"]
dependency_heuristic = "semantic-curriculum-review-v1"
dependency_review_count = 1
+++

Let \(B\) be a symmetric [[linear-algebra/bilinear-form|bilinear form]] on a finite-dimensional real [[linear-algebra/vector-space|vector space]]. There is a basis in which
\[
B(x,x)=-x_1^2-\cdots-x_p^2+x_{p+1}^2+\cdots+x_{p+q}^2,
\]
with \(r=\dim V-p-q\) additional zero directions. In this collection, the triple \((p,q,r)\) is the **inertia** of \(B\), ordered as the numbers of negative, positive, and zero squares. For a nondegenerate form, \(r=0\), and the pair \((p,q)\), again with negative directions first, is its **signature**.

## Convention warning

Many texts instead list positive directions first, and some call the difference between the two counts the signature. A signature convention should therefore be stated explicitly, especially in Lorentzian geometry.

## Basis independence

Sylvester's law of inertia says that \(p,q,r\) do not depend on the diagonalizing basis. Equivalently, they are the numbers of negative, positive, and zero eigenvalues of any representing real symmetric matrix, counted with multiplicity.

## Relation to quadratic forms

The associated [[linear-algebra/quadratic-form|quadratic form]] is \(q(v)=B(v,v)\). In the convention of this collection, positive-definite forms have signature \((0,\dim V)\), negative-definite forms have signature \((\dim V,0)\), and the Lorentzian form \(\operatorname{diag}(-1,1,\ldots,1)\) has signature \((1,n-1)\).

## References

1. Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed., Cambridge University Press, 2013. [DOI record](https://doi.org/10.1017/CBO9781139020411). Relevant: Hermitian and symmetric matrices, congruence, and inertia.
