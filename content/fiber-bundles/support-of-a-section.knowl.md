+++
id = "fiber-bundles/support-of-a-section"
title = "Support of a section"
kind = "definition"
summary = "The closure of the set of base points where a vector bundle section is nonzero."
aliases = ["section support", "support of a vector bundle section"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/vector-bundle", "fiber-bundles/section-of-a-vector-bundle", "topology/closed-set"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(E\to M\) be a smooth [[fiber-bundles/vector-bundle|vector bundle]] and \(s\in\Gamma^\infty(M,E)\) a smooth [[fiber-bundles/section-of-a-vector-bundle|section]]. The **support of \(s\)** is the [[topology/closed-set|closed set]]
\[
\operatorname{supp}(s)
=
\overline{\{x\in M:s(x)\neq 0_x\}},
\]
where \(0_x\) is the zero vector in \(E_x\). Equivalently, \(x\notin\operatorname{supp}(s)\) exactly when \(s\) vanishes identically on some neighborhood of \(x\). The section is **compactly supported** when \(\operatorname{supp}(s)\) is compact; the space of such sections is denoted \(\Gamma_c^\infty(M,E)\).

## Local description

In a local frame \(e_1,\ldots,e_r\), write \(s=\sum_i s^i e_i\). Then
\[
\operatorname{supp}(s)\cap U
=
\bigcup_{i=1}^r\bigl(\operatorname{supp}(s^i)\cap U\bigr).
\]
Hence support is independent of the chosen frame. The closure in the definition matters: the nonzero locus is open, but points where nonzero values accumulate belong to the support even when the section itself vanishes there.

## Basic operations

For [[fiber-bundles/section-of-a-fiber-bundle|smooth sections]] \(s,t\) and a smooth function \(f\),
\[
\operatorname{supp}(s+t)\subseteq
\operatorname{supp}(s)\cup\operatorname{supp}(t),
\qquad
\operatorname{supp}(fs)\subseteq
\operatorname{supp}(f)\cap\operatorname{supp}(s).
\]
These inclusions can be strict because of cancellation or extra zeros. A [[fiber-bundles/vector-bundle-morphism|vector bundle morphism]] over \(M\) cannot enlarge support: \(\operatorname{supp}(\Phi\circ s)\subseteq\operatorname{supp}(s)\).

Compact support makes local constructions global. If a section is supported in a trivializing open set, it can be represented by compactly supported component functions there and extended by zero outside that open set, provided its support stays away from the boundary.

## Conventions and scope

Some authors call \(\{x:s(x)\neq0_x\}\) the support before taking its closure, but the closed-support convention used here is standard in analysis and differential geometry. The support is a subset of the base \(M\), not the image \(s(M)\subseteq E\). For sections of affine or general fiber bundles, “nonzero” requires a separately chosen reference section and is therefore not intrinsic.

## References

1. J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 2, supports, bump functions, and partitions of unity.
2. L. W. Tu, *An Introduction to Manifolds*, 2nd ed., Springer, 2011. [DOI record](https://doi.org/10.1007/978-1-4419-7400-6). Relevant: Chapter 13, compact supports and integration.
