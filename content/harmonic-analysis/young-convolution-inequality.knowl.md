+++
id = "harmonic-analysis/young-convolution-inequality"
title = "Young's convolution inequality"
kind = "theorem"
summary = "Young's convolution inequality bounds the Lp norm of a convolution by the product of the norms of its factors."
aliases = ["Young inequality for convolution", "Lp convolution estimate"]
domains = ["harmonic-analysis", "functional-analysis", "measure-theory"]
prerequisites = ["harmonic-analysis/unimodular-group", "topology/locally-compact-group", "harmonic-analysis/haar-measure", "harmonic-analysis/convolution-on-locally-compact-group", "algebra-modules/bilinear-map", "convex-analysis/holder-inequality-integrals", "measure-theory/tonellis-theorem"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(G\) be a [[harmonic-analysis/unimodular-group|unimodular]] [[topology/locally-compact-group|locally compact group]] with a fixed [[harmonic-analysis/haar-measure|Haar measure]]. Suppose \(1\leq p,q,r\leq\infty\) satisfy
\[
\frac1p+\frac1q=1+\frac1r.
\]
For \(f\in L^p(G)\) and \(g\in L^q(G)\), their [[harmonic-analysis/convolution-on-locally-compact-group|convolution]], initially defined where the integral exists, has an \(L^r(G)\) representative and obeys **Young's convolution inequality**
\[
\lVert f*g\rVert_r\leq \lVert f\rVert_p\lVert g\rVert_q.
\]
Consequently convolution extends uniquely to a bounded [[algebra-modules/bilinear-map|bilinear map]] \(L^p(G)\times L^q(G)\to L^r(G)\).

## Endpoint estimates

The case \(p=1\) and \(q=r\) says that averaging left translates of \(g\) against \(f\) costs at most \(\lVert f\rVert_1\). The case \(p=q=2\), \(r=\infty\), follows directly from the integral [[convex-analysis/holder-inequality-integrals|Hölder inequality]]. Taking \(p=q=r=1\) proves that \(L^1(G)\) is closed under convolution and supplies its [[functional-analysis/banach-algebra|Banach-algebra]] norm estimate.

## Proof mechanism and extension

For compactly supported continuous functions, translation invariance of Haar measure, Hölder's inequality, and [[measure-theory/tonellis-theorem|Tonelli's theorem]] give the endpoint bounds. Interpolation and density yield the remaining exponent range. The extension is independent of the approximating functions because the displayed estimate makes convolution jointly continuous in the indicated norms.

## Scope and nonunimodular groups

Euclidean Young inequality is the case \(G=\mathbb R^n\). The same constant-one estimate holds on discrete groups with counting measure and on compact groups with normalized Haar measure.

**Warning.** On a nonunimodular group, [[lie-groups/right-translation|right translations]] change a left Haar measure. Some exponent arrangements therefore require a power of the [[harmonic-analysis/modular-function|modular function]] or a different left/right convolution convention. The unimodularity hypothesis in the core avoids suppressing that correction.

## References

1. G. B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016. [DOI record](https://doi.org/10.1201/B19172). Relevant: Chapter 2, convolution estimates on locally compact groups.
2. E. Hewitt and K. A. Ross, *Abstract Harmonic Analysis*, Volume I, Springer, 1963. [DOI record](https://doi.org/10.1007/978-3-662-40409-6). Relevant: convolution and \(L^p\)-space inequalities.
