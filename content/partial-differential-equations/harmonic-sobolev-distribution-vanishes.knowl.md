+++
id = "partial-differential-equations/harmonic-sobolev-distribution-vanishes"
title = "A harmonic global Sobolev distribution vanishes"
kind = "theorem"
summary = "A harmonic distribution in an inhomogeneous Hs space on the whole Euclidean space is zero."
aliases = ["harmonic negative Sobolev uniqueness"]
domains = ["partial-differential-equations"]
section_mode = "progressive"
prerequisites = ["partial-differential-equations/harmonic-distribution", "functional-analysis/fourier-sobolev-space", "functional-analysis/support-of-distribution", "measure-theory/null-set"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

If \(h\in H^s(\mathbb R^n)\) for some real \(s\) and \(\Delta h=0\) in distributions, then \(h=0\). This uses the whole-space [[functional-analysis/fourier-sobolev-space|inhomogeneous Sobolev space]], including its condition at zero frequency.

## Fourier proof

Fourier transformation gives \(|\xi|^2\widehat h=0\). On any open set disjoint from zero one can divide a test function by \(|\xi|^2\), proving that \(\widehat h\) is supported at \(\{0\}\). But \(\widehat h\) is represented by a locally square-integrable function. Such a function supported on the measure-zero set \(\{0\}\) vanishes almost everywhere. Fourier inversion gives \(h=0\).

## Why the hypothesis matters

Nonzero constants are harmonic tempered distributions, yet belong to no global inhomogeneous \(H^s\). One cannot replace the stated Sobolev membership by temperateness or by local Sobolev membership.
