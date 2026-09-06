+++
id = "convex-analysis/pluripotential-valuation-construction"
title = "Pluripotential construction of convex-body valuations"
kind = "theorem"
summary = "Complex and quaternionic Hessian measures of support functions define continuous translation-invariant valuations."
aliases = ["PSH construction of valuations", "Hessian-measure valuation construction"]
domains = ["convex-analysis", "complex-analysis", "quaternionic-analysis"]
section_mode = "progressive"
prerequisites = ["convex-analysis/support-function", "convex-analysis/valuation-on-convex-bodies"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(K\mapsto h_K\) be the
[[convex-analysis/support-function|support-function]] embedding of convex
bodies. Integrating a compactly supported test object against a fixed-degree
complex or quaternionic Hessian measure of \(h_K\) defines a continuous
translation-invariant [[convex-analysis/valuation-on-convex-bodies|valuation]].

In the quaternionic case, for suitable compactly supported data
\(V^{(1)},\ldots,V^{(n-k)}\) and \(\psi\), a representative family is
\[
K\longmapsto
\int_{(\mathbb H^n)^*}
D\!\left((\operatorname{Hess}_{\mathbb H}h_K)[k],
V^{(1)},\ldots,V^{(n-k)}\right)\psi\,dV.
\]

## Why it is continuous

[[topology/hausdorff-distance|Hausdorff convergence]] \(K_m\to K\) gives
locally [[real-analysis/uniform-convergence|uniform convergence]]
\(h_{K_m}\to h_K\). The
[[complex-analysis/quaternionic-monge-ampere-continuity-theorem|continuity of
quaternionic Monge–Ampère measures]] then gives convergence of the displayed
integrals.

## Why it is a valuation

When \(K\cup L\) is convex, support functions convert union and intersection
into maximum and minimum. The
[[complex-analysis/quaternionic-blocki-formula|quaternionic Błocki formula]]
converts those max/min operations into inclusion–exclusion for the Hessian
measures. Translation adds a linear function to \(h_K\), which its Hessian
annihilates.

## Complex, quaternionic, and octonionic branches

The complex construction uses powers of \(dd^ch_K\) paired with compactly
supported forms. The quaternionic construction uses
[[linear-algebra/mixed-discriminant|mixed Moore determinants]].
On \(\mathbb O^2\), the analogous determinant measure produces the
[[convex-analysis/octonionic-pseudovolume|octonionic pseudovolume]]. These are
parallel mechanisms with different underlying Hessians.

## References

1. Semyon Alesker, “Valuations on convex sets, non-commutative determinants, and pluripotential theory,” *Advances in Mathematics* 195 (2005), 561–595. [arXiv record](https://arxiv.org/abs/math/0401219). Relevant: Theorems 4.1.3 and 4.2.1.
2. Semyon Alesker, “Quaternionic plurisubharmonic functions and their applications to convexity,” 2016 revision. [arXiv record](https://arxiv.org/abs/math/0606756). Relevant: §4.
