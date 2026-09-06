+++
id = "analysis/porosity-on-balls"
title = "Porosity on balls"
kind = "definition"
summary = "A quantitative hole condition requiring every ball in a range of scales to contain a comparably sized ball disjoint from the set."
aliases = ["ball porosity", "porous on balls", "nu-porous on balls"]
domains = ["analysis", "geometric-measure-theory", "harmonic-analysis"]
prerequisites = []
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(0<\nu\le 1\) and \(0<\alpha_0<\alpha_1\). A set
\(X\subseteq\mathbb R^d\) is **\(\nu\)-porous on balls from scales
\(\alpha_0\) to \(\alpha_1\)** if every Euclidean ball \(B\) whose diameter
\(R\) satisfies \(\alpha_0<R<\alpha_1\) contains a point \(x\in B\) such that
\[
B_{\nu R}(x)\cap X=\varnothing.
\]
Thus every admissible observation ball contains a hole whose radius is a fixed
fraction of the observation scale.

## Scale dependence

Porosity here is explicitly truncated: nothing is required below
\(\alpha_0\) or above \(\alpha_1\). This is the form used in quantitative
[[harmonic-analysis/fractal-uncertainty-principle|fractal uncertainty
principles]], where the smallest scale is tied to a semiclassical parameter.

## Relation to other notions

[[analysis/porosity-on-lines|Porosity on lines]] tests every line segment and
is stronger in dimensions at least two. In one dimension the two definitions
agree up to the harmless convention of using radius or diameter as the scale.
Porosity also forces quantitative decay of [[measure-theory/lebesgue-measure|Lebesgue measure]] through the
[[analysis/porous-set-measure-decay|porous-set measure-decay estimate]].

## References

1. Alex Cohen, “Fractal uncertainty in higher dimensions,” 2024. [arXiv record](https://arxiv.org/abs/2305.05022). Relevant: §§1.2 and A.2.
