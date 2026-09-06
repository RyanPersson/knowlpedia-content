+++
id = "complex-analysis/analytic-continuation"
title = "Analytic continuation"
kind = "definition"
summary = "Extension of a holomorphic function through overlapping domains, uniquely controlled by the identity theorem."
aliases = ["holomorphic continuation"]
domains = ["complex-analysis"]
section_mode = "progressive"
prerequisites = ["complex-analysis/complex-domain", "topology/connected-component", "complex-analysis/identity-theorem"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(U\) and \(V\) be [[complex-analysis/complex-domain|complex domains]], and let \(C\) be a [[topology/connected-component|connected component]] of \(U\cap V\). A holomorphic function \(g:V\to\mathbb C\) is an **analytic continuation** of a holomorphic function \(f:U\to\mathbb C\) through \(C\) if \(f=g\) on \(C\). By the [[complex-analysis/identity-theorem|identity theorem]], it is enough to require equality on any nonempty open subset of \(C\).

Specifying the component matters when \(U\cap V\) is disconnected: agreement on one component does not force agreement on the others. When the overlap is connected, one simply says that \(g\) is an analytic continuation of \(f\) through \(U\cap V\).

## Along a path

Continuation along a path is described by a chain of overlapping discs and holomorphic functions that agree successively. Its endpoint value can depend on the path when the ambient domain is not [[topology/simply-connected-space|simply connected]]. The [[complex-analysis/monodromy-theorem|monodromy theorem]] supplies path independence under suitable simple-connectivity hypotheses.

## Germ viewpoint

A [[complex-analysis/holomorphic-germ|holomorphic germ]] at \(a\) is an equivalence class of holomorphic functions defined near \(a\), where two representatives agree on some smaller neighborhood. Analytic continuation transports such germs. Singularities and nontrivial monodromy may obstruct a single-valued global continuation even when continuation is possible along every short segment.

## References

1. Otto Forster, *Lectures on Riemann Surfaces*, Springer, 1981. [Publisher record](https://doi.org/10.1007/978-1-4612-5961-9). Relevant: Chapter 1, §§5–7.
