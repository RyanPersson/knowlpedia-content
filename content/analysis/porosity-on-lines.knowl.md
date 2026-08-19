+++
id = "analysis/porosity-on-lines"
title = "Porosity on lines"
kind = "definition"
summary = "A quantitative hole condition imposed on every line segment in a prescribed range of scales."
aliases = ["line porosity", "line porous set", "porous on lines", "nu-porous on lines"]
domains = ["analysis", "geometric-measure-theory", "harmonic-analysis"]
section_mode = "progressive"
+++

Let \(0<\nu\le 1\) and \(0<\alpha_0<\alpha_1\). A set
\(Y\subseteq\mathbb R^d\) is **\(\nu\)-porous on lines from scales
\(\alpha_0\) to \(\alpha_1\)** if, for every line segment \(\tau\) of length
\(R\) with \(\alpha_0<R<\alpha_1\), some \(x\in\tau\) satisfies
\[
B_{\nu R}(x)\cap Y=\varnothing.
\]
The missing ball may extend away from the line, but its center must lie on the
tested segment.

## Why this is stronger than ball porosity

Every line-porous set is [[analysis/porosity-on-balls|porous on balls]], after
an inessential adjustment of constants. The converse fails for \(d\ge2\): a
straight line has large holes inside ambient balls but has none along segments
lying in that line. Line porosity therefore excludes orthogonal linear
concentrations that obstruct higher-dimensional uncertainty estimates.

## Stability properties

Dilating \(Y\) by \(s>0\) multiplies both endpoint scales by \(s\) and preserves
\(\nu\). Intersecting with any fixed line produces a one-dimensional porous
set. A sufficiently small [[analysis/minkowski-thickening|Minkowski
thickening]] remains line porous with a smaller porosity constant and a larger
lower scale.

## References

1. Alex Cohen, “Fractal uncertainty in higher dimensions,” 2024. [arXiv record](https://arxiv.org/abs/2305.05022). Relevant: §§1.2 and A.2.
