+++
id = "convex-analysis/support-function"
title = "Support function of a convex body"
kind = "definition"
summary = "The sublinear function recording the maximal value of each linear functional on a convex body."
aliases = ["supporting functional of a convex body", "support function", "h_K"]
domains = ["convex-analysis", "integral-geometry"]
prerequisites = ["convex-analysis/convex-body", "linear-algebra/inner-product"]
dependency_review_count = 1
section_mode = "progressive"
+++

For a [[convex-analysis/convex-body|convex body]] \(K\subseteq V\), its
**support function** is
\[
h_K:V^*\longrightarrow\mathbb R,
\qquad h_K(\ell)=\sup_{x\in K}\ell(x).
\]
After choosing an [[linear-algebra/inner-product|inner product]] and identifying
\(V^*\cong V\), this becomes
\(h_K(y)=\sup_{x\in K}\langle x,y\rangle\).

## Characterization

The support function is finite, continuous, positively homogeneous, and
subadditive. Conversely, every finite continuous sublinear function on
\(V^*\) is the support function of a unique convex body. Thus \(h_K\)
determines \(K\).

## Operations

For \(s,t\ge0\),
\[
h_{sK+tL}=s h_K+t h_L.
\]
Translations add a linear function:
\(h_{K+a}(\ell)=h_K(\ell)+\ell(a)\). If \(K\cup L\) is convex, then
\[
h_{K\cup L}=\max(h_K,h_L),
\qquad h_{K\cap L}=\min(h_K,h_L).
\]
The max/min identities connect Hessian measures to
[[convex-analysis/valuation-on-convex-bodies|valuations]].

## Plurisubharmonic viewpoint

Because \(h_K\) is convex, it is subharmonic and, on complex, quaternionic, or
the octonionic plane, belongs to the corresponding plurisubharmonic class.
Its Hessian measure can therefore be used in the
[[convex-analysis/pluripotential-valuation-construction|pluripotential
construction of valuations]].

## References

1. Rolf Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, 2nd ed., Cambridge University Press, 2014. [DOI record](https://doi.org/10.1017/CBO9781139003858). Relevant: §1.7.
