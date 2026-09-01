+++
id = "algebraic-geometry-foundations/small-etale-site"
title = "Small étale site"
kind = "knowl"
summary = "The site of schemes étale over a fixed scheme, covered by jointly surjective étale families."
aliases = ["small-etale-site", "Small etale site", "Small étale site"]
domains = ["algebraic-geometry-foundations"]
prerequisites = ["algebraic-geometry-foundations/scheme", "algebraic-geometry-foundations/site", "algebraic-geometry-foundations/etale-morphism", "algebraic-geometry-foundations/scheme-over-a-base"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
+++

Let \(X\) be a [[algebraic-geometry-foundations/scheme|scheme]]. The **small étale site** \(X_{\acute et}\) is the [[algebraic-geometry-foundations/site|site]] defined as follows:

- its objects are [[algebraic-geometry-foundations/etale-morphism|étale morphisms]] \(U\to X\);
- a morphism from \(V\to X\) to \(U\to X\) is an [[algebraic-geometry-foundations/scheme-over-a-base|\(X\)-morphism]] \(V\to U\);
- a family \(\{U_i\to U\}\) is covering when every map is étale and the family is jointly surjective on underlying points.

The word **small** means that only schemes étale over the fixed base \(X\) are used as objects, rather than all schemes over \(X\).

When \(X=\operatorname{Spec}F\) for a field \(F\), every finite separable extension \(K/F\) supplies a covering object \(\operatorname{Spec}K\to X\). This is the local setting in which a finite Galois extension becomes a torsor.
