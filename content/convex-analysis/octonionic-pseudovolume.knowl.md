+++
id = "convex-analysis/octonionic-pseudovolume"
title = "Octonionic pseudovolume"
kind = "construction"
summary = "A Spin(9)-invariant continuous valuation obtained from the octonionic Hessian measure of a support function."
aliases = ["octonionic pseudo-volume", "Spin(9)-invariant octonionic valuation", "P_O valuation"]
domains = ["convex-analysis", "octonionic-analysis", "lie-groups"]
section_mode = "progressive"
+++

Let \(K\subseteq\mathbb O^2\cong\mathbb R^{16}\) be a
[[convex-analysis/convex-body|convex body]], let \(h_K\) be its
[[convex-analysis/support-function|support function]], and let \(B\) be the
centered unit ball. The **octonionic pseudovolume** is
\[
P_{\mathbb O}(K)=
\int_B \det\!\left(\operatorname{Hess}_{\mathbb O}h_K\right)dq,
\]
with the Hessian determinant interpreted as the
[[complex-analysis/octonionic-monge-ampere-measure|octonionic Monge–Ampère
measure]].

## Valuation and invariance

The functional \(P_{\mathbb O}\) is a continuous translation-invariant
[[convex-analysis/valuation-on-convex-bodies|valuation]] and is invariant
under the [[lie-groups/spin9-spin-representation|\(\operatorname{Spin}(9)\)
spin action]] on \(\mathbb O^2\).

## Mechanism

Continuity follows because [[topology/hausdorff-distance|Hausdorff convergence]]
of convex bodies gives locally
[[real-analysis/uniform-convergence|uniform convergence]] of support functions
and hence weak convergence of their
[[complex-analysis/octonionic-monge-ampere-measure|octonionic Hessian
measures]]. The valuation identity follows from the
max-min formula for those measures. Translation invariance follows because
translating \(K\) adds a linear function to \(h_K\), leaving its Hessian
unchanged.

## General test functions

More generally, integrating the Hessian measure against any compactly
supported continuous test function gives a continuous translation-invariant
valuation. Choosing the radial test function \(1_B\) exposes the full
\(\operatorname{Spin}(9)\) symmetry and yields \(P_{\mathbb O}\).

## References

1. Semyon Alesker, “Plurisubharmonic functions on the octonionic plane and \(\operatorname{Spin}(9)\)-invariant valuations on convex sets,” *Journal of Geometric Analysis* 18 (2008), 651–686. [arXiv record](https://arxiv.org/abs/0707.4385). Relevant: Theorem 0.1.8 and §4.
