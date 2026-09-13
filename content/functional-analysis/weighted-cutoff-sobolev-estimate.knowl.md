+++
id = "functional-analysis/weighted-cutoff-sobolev-estimate"
title = "Sobolev estimate with a scaled cutoff"
kind = "theorem"
summary = "A localized L6 norm is controlled by the localized gradient and a scale-weighted L2 norm."
aliases = []
domains = ["functional-analysis"]
section_mode = "progressive"
prerequisites = ["functional-analysis/three-dimensional-sobolev-inequality", "real-analysis/cutoff-function", "real-analysis/product-rule", "measure-theory/lp-space", "functional-analysis/local-sobolev-space"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 2
+++

Let \(\phi\in C_c^\infty(\mathbb R^3)\), \(0\le\phi\le1\), and \(\phi_R(x)=\phi(x/R)\). For an integer \(m\ge1\) and \(u\in L^2\cap H^1_{\mathrm{loc}}\),
\[
\|\phi_R^m u\|_6\le C_{m,\phi}\bigl(\|\phi_R^m\nabla u\|_2+R^{-1}\|u\|_2\bigr).
\]
Here \(H^1_{\mathrm{loc}}\) denotes [[functional-analysis/local-sobolev-space|local Sobolev membership]]. No global gradient bound is assumed.

## Product rule

Apply the [[functional-analysis/three-dimensional-sobolev-inequality|three-dimensional Sobolev inequality]] to the compactly supported \(H^1\) function \(\phi_R^m u\). Its gradient is \(\phi_R^m\nabla u+m\phi_R^{m-1}(\nabla\phi_R)u\), and the second term is bounded in \(L^2\) by \(C R^{-1}\|u\|_2\).
