+++
id = "analysis/ahlfors-david-regular-set"
title = "Ahlfors–David regular set"
kind = "definition"
summary = "A set carrying a measure whose mass in centered balls is uniformly comparable to a fixed power of the radius."
aliases = ["AD-regular set", "Ahlfors regular set", "delta-regular set"]
domains = ["analysis", "geometric-measure-theory", "measure-theory"]
prerequisites = ["measure-theory/measure"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(0\le\delta\le d\), \(C\ge1\), and
\(0<\alpha_0<\alpha_1\). A set \(X\subseteq\mathbb R^d\) is
**Ahlfors–David \(\delta\)-regular with constant \(C\) from scales
\(\alpha_0\) to \(\alpha_1\)** if there is a [[measure-theory/measure|measure]]
\(\mu\) supported on \(X\) such that every ball \(B\) of diameter
\(\alpha_0<R<\alpha_1\) satisfies
\[
\mu(B)\le C R^\delta,
\]
and, whenever the center of \(B\) lies in \(X\), also
\[
\mu(B)\ge C^{-1}R^\delta.
\]

## Interpretation

The exponent \(\delta\) is a uniform effective dimension throughout the
specified scale range. The upper bound prevents excessive concentration; the
centered lower bound prevents large holes relative to the support.

## Relation to porosity

On the real line, an Ahlfors–David regular set of dimension \(\delta<1\) is
[[analysis/porosity-on-balls|porous]], with constants depending on \(C\) and
\(\delta\). Conversely, a truncated porous subset of \(\mathbb R\) can be
enlarged to a regular set of some dimension below one. In higher dimensions,
regularity and [[analysis/porosity-on-lines|line porosity]] are distinct.

## References

1. Pertti Mattila, *Geometry of Sets and Measures in Euclidean Spaces*, Cambridge University Press, 1995. [DOI record](https://doi.org/10.1017/CBO9780511623813).
2. Alex Cohen, “Fractal uncertainty in higher dimensions,” 2024. [arXiv record](https://arxiv.org/abs/2305.05022). Relevant: §1.3.
