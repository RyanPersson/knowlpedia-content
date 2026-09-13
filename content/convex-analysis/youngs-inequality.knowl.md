+++
id = "convex-analysis/youngs-inequality"
title = "Young's Inequality"
kind = "knowl"
summary = "A conjugate-exponent bound: |xy| is controlled by |x|^p/p + |y|^q/q"
aliases = ["youngs-inequality", "Young's Inequality"]
domains = ["convex-analysis"]
legacy_source_path = "convex-analysis/youngs-inequality.md"
prerequisites = ["real-analysis/absolute-value", "convex-analysis/weighted-arithmeticgeometric-mean-inequality", "real-analysis/real-power"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 3
+++

**Young's Inequality**: Let \(p,q>1\) satisfy \(\frac1p+\frac1q=1\). Then for all \(x,y\in\mathbb{R}\),
\[
|xy|\le \frac{|x|^p}{p}+\frac{|y|^q}{q}.
\]

## Examples

- If \(p=q=2\), then \(|xy|\le \frac{x^2}{2}+\frac{y^2}{2}\).
- If \(p=3\) and \(q=\frac32\), then \(|xy|\le \frac{|x|^3}{3}+\frac{2|y|^{3/2}}{3}\).

## Remarks

This inequality is a standard tool behind [[convex-analysis/holder-inequality-finite-sums|Hölder's inequality]], [[convex-analysis/holder-inequality-integrals|Hölder's inequality for integrals]], and many estimates in [[convex-analysis|convex analysis]]. In the lecture notes it is obtained from the [[convex-analysis/weighted-arithmeticgeometric-mean-inequality|weighted AM–GM inequality]] applied to \(a=|x|^p\) and \(b=|y|^q\).

## A small coefficient for absorption

Replacing \(x\) by \(\varepsilon^{1/p}x\) and \(y\) by \(\varepsilon^{-1/p}y\) gives, for \(\varepsilon>0\),
\[
|xy|\le\frac{\varepsilon}{p}|x|^p+
\frac{\varepsilon^{-q/p}}q|y|^q.
\]
For quadratic estimates one often writes the equivalent form
\(|xy|\le\varepsilon x^2+y^2/(4\varepsilon)\), which also follows by expanding \((\sqrt\varepsilon |x|-|y|/(2\sqrt\varepsilon))^2\ge0\).
