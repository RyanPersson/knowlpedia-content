+++
id = "complex-analysis/quaternionic-blocki-formula"
title = "Quaternionic Błocki formula"
kind = "theorem"
summary = "An inclusion–exclusion identity for quaternionic Monge–Ampère measures under maxima and minima."
aliases = ["quaternionic max-min Monge-Ampere formula", "quaternionic Błocki identity"]
domains = ["complex-analysis", "quaternionic-analysis", "potential-theory"]
prerequisites = ["complex-analysis/quaternionic-plurisubharmonic-function"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(u,v\) be continuous
[[complex-analysis/quaternionic-plurisubharmonic-function|quaternionic
plurisubharmonic functions]] on \(\Omega\subseteq\mathbb H^n\), and assume
that \(\min\{u,v\}\) is also quaternionic PSH. Then
\[
\operatorname{MA}_{\mathbb H}(\max\{u,v\})
+\operatorname{MA}_{\mathbb H}(\min\{u,v\})
=\operatorname{MA}_{\mathbb H}(u)+\operatorname{MA}_{\mathbb H}(v).
\]
There are corresponding polarized identities for mixed quaternionic
Monge–Ampère measures.

## Why the minimum is an hypothesis

The maximum of two quaternionic PSH functions is again quaternionic PSH, but
their minimum need not be. The displayed identity therefore cannot be stated
for an arbitrary pair without the extra assumption.

## Role in valuation theory

For [[convex-analysis/support-function|support functions]] of
[[convex-analysis/convex-body|convex bodies]],
\(h_{K\cup L}=\max(h_K,h_L)\) when \(K\cup L\) is convex, and
\(h_{K\cap L}=\min(h_K,h_L)\). The formula turns this max/min behavior into
the inclusion–exclusion identity for a
[[convex-analysis/valuation-on-convex-bodies|valuation on convex bodies]].

## References

1. Zbigniew Błocki, “On the definition of the Monge–Ampère operator in \(\mathbb C^2\),” *Mathematische Annalen* 328 (2004), 415–423. [DOI record](https://doi.org/10.1007/s00208-003-0491-0).
2. Semyon Alesker, “Valuations on convex sets, non-commutative determinants, and pluripotential theory,” *Advances in Mathematics* 195 (2005), 561–595. [arXiv record](https://arxiv.org/abs/math/0401219). Relevant: Theorem 3.2.1.
