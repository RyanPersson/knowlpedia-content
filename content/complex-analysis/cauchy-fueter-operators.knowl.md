+++
id = "complex-analysis/cauchy-fueter-operators"
title = "Cauchy–Fueter operators"
kind = "definition"
summary = "The first-order quaternionic differential operators analogous to the complex d-bar and d operators."
aliases = ["quaternionic Dirac operators", "Cauchy-Fueter operator", "quaternionic d-bar operator"]
domains = ["complex-analysis", "quaternionic-analysis", "partial-differential-equations"]
prerequisites = []
dependency_review_count = 1
section_mode = "progressive"
+++

Write \(q=t+xi+yj+zk\in\mathbb H\). For a smooth quaternion-valued function
\(F\), the **Cauchy–Fueter operators** in the convention used here are
\[
\frac{\partial F}{\partial\bar q}
=\partial_tF+i\partial_xF+j\partial_yF+k\partial_zF,
\qquad
\frac{\partial F}{\partial q}
=\partial_tF-\partial_xF\,i-\partial_yF\,j-\partial_zF\,k.
\]
In several quaternionic variables one applies these formulas to each
coordinate.

## Relation to the Laplacian

On real-valued functions, the appropriate compositions recover the Euclidean
Laplacian on \(\mathbb R^4\), up to the normalization built into the displayed
operators. Mixed derivatives form the
[[complex-analysis/quaternionic-hessian|quaternionic Hessian]].

## Convention warning

Because \(\mathbb H\) is noncommutative, left and right placement of the units
\(i,j,k\) matters. Authors also insert factors such as \(1/2\). A formula using
\(\partial_q\) or \(\partial_{\bar q}\) must therefore state its convention;
the two displayed operators are not obtained by treating quaternionic
coefficients as if they commute.

## References

1. Semyon Alesker, “Non-commutative linear algebra and plurisubharmonic functions of quaternionic variables,” *Bulletin des Sciences Mathématiques* 127 (2003), 1–35. [arXiv record](https://arxiv.org/abs/math/0104209). Relevant: §2.
2. Semyon Alesker, “Quaternionic plurisubharmonic functions and their applications to convexity,” 2016 revision. [arXiv record](https://arxiv.org/abs/math/0606756). Relevant: §2.
