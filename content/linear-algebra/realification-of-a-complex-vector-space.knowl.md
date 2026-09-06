+++
id = "linear-algebra/realification-of-a-complex-vector-space"
title = "Realification of a complex vector space"
kind = "construction"
summary = "A complex vector space regarded as a real vector space by restriction of scalars."
aliases = ["underlying real vector space", "restriction of scalars from complex to real"]
domains = ["linear-algebra"]
prerequisites = ["linear-algebra/vector-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(V\) be a complex [[linear-algebra/vector-space|vector space]]. Its **realification** \(V_{\mathbb R}\) is the same additive group, regarded as a real vector space by restricting scalar multiplication along \(\mathbb R\hookrightarrow\mathbb C\). If \(\dim_{\mathbb C}V=n<\infty\), then
\[
\dim_{\mathbb R}V_{\mathbb R}=2n.
\]

## Complex structure retained as an operator

Multiplication by \(i\) becomes a real-linear endomorphism
\[
J:V_{\mathbb R}\to V_{\mathbb R},\qquad J^2=-\operatorname{id}.
\]
Conversely, a real vector space equipped with such an operator \(J\) becomes a complex vector space by defining \((a+ib)v=av+bJv\).

## Functoriality

Every complex-linear map \(f:V\to W\) is real-linear after realification and commutes with \(J\). Not every real-linear map \(V_{\mathbb R}\to W_{\mathbb R}\) arises this way: the additional condition is \(fJ_V=J_Wf\).

## References

1. Steven Roman, *Advanced Linear Algebra*, 3rd ed., Springer, 2008. [DOI record](https://doi.org/10.1007/978-0-387-72831-5). Relevant: restriction of scalars and complex structures.
