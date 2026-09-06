+++
id = "algebra-fields-galois/non-archimedean-absolute-value"
title = "Non-Archimedean absolute value"
kind = "definition"
summary = "A multiplicative absolute value satisfying the strong triangle inequality."
aliases = ["ultrametric absolute value", "nonarchimedean norm on a field"]
domains = ["algebra-fields-galois", "real-analysis"]
prerequisites = ["algebra-fields-galois/valuation-on-a-field"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

A **non-Archimedean absolute value** on a field \(K\) is a map
\[
|\cdot|:K\longrightarrow\mathbb R_{\geq0}
\]
such that
\[
|x|=0\Longleftrightarrow x=0,\qquad |xy|=|x||y|,\qquad
|x+y|\leq\max\{|x|,|y|\}.
\]
The last condition is the **strong triangle inequality**.

It induces the ultrametric \(d(x,y)=|x-y|\). If
\(v:K\to\mathbb R\cup\{\infty\}\) is an additive
[[algebra-fields-galois/valuation-on-a-field|valuation]], then
\[
|x|=e^{-v(x)}
\]
is a non-Archimedean absolute value. Conversely, taking
\(-\log|x|\) recovers an additive real-valued valuation.

## References
Oleg Viro, “Hyperfields for Tropical Geometry I: Hyperfields and
dequantization,” 2010. [arXiv:1006.3034](https://arxiv.org/abs/1006.3034).
