+++
id = "analysis/minkowski-thickening"
title = "Minkowski thickening"
kind = "construction"
summary = "The closed or open metric neighborhood obtained by adding a radius-r ball to a set."
aliases = ["r-neighborhood of a set", "parallel set", "Minkowski neighborhood"]
domains = ["analysis", "topology", "convex-analysis"]
section_mode = "progressive"
prerequisites = ["convex-analysis/minkowski-sum", "topology/closed-ball"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

For \(X\subseteq\mathbb R^d\) and \(r>0\), the **Minkowski thickening** of \(X\)
by radius \(r\) is the [[convex-analysis/minkowski-sum|Minkowski sum]]
\[
X+B_r=\{x+b:x\in X, |b|<r\}.
\]
Equivalently, it is the open \(r\)-neighborhood
\(\{z:\operatorname{dist}(z,X)<r\}\). Using the [[topology/closed-ball|closed ball]] produces the
closed thickening and changes only boundary conventions.

## Scaling and translation

For \(s>0\), \(s(X+B_r)=sX+B_{sr}\). Translation commutes with thickening.
These identities make the construction natural in multiscale estimates.

## Effect on porosity

If \(X\) is \(\nu\)-[[analysis/porosity-on-lines|porous on lines]] and
\(0<\nu'<\nu\), then \(X+B_r\) remains \(\nu'\)-porous on segments of length
larger than \(r/(\nu-\nu')\), as long as the original upper scale is respected.

## References

1. Rolf Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, 2nd ed., Cambridge University Press, 2014. [DOI record](https://doi.org/10.1017/CBO9781139003858).
