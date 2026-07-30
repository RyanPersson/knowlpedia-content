+++
id = "complex-analysis/analytic-continuation"
title = "Analytic continuation"
kind = "definition"
summary = "Extension of a holomorphic function through overlapping domains, uniquely controlled by the identity theorem."
aliases = ["holomorphic continuation"]
domains = ["complex-analysis"]
section_mode = "progressive"
+++

Let \(U\) and \(V\) be [[complex-analysis/complex-domain|complex domains]] with nonempty intersection. A holomorphic function \(g:V\to\mathbb C\) is an **analytic continuation** of a holomorphic function \(f:U\to\mathbb C\) through the overlap if \(f=g\) on a nonempty open subset of \(U\cap V\). The [[complex-analysis/identity-theorem|identity theorem]] then forces equality on every connected component of the overlap reached by that subset.

## Along a path

Continuation along a path is described by a chain of overlapping discs and holomorphic functions that agree successively. Its endpoint value can depend on the path when the ambient domain is not simply connected. The [[complex-analysis/monodromy-theorem|monodromy theorem]] supplies path independence under suitable simple-connectivity hypotheses.

## Germ viewpoint

A [[complex-analysis/holomorphic-germ|holomorphic germ]] at \(a\) is an equivalence class of holomorphic functions defined near \(a\), where two representatives agree on some smaller neighborhood. Analytic continuation transports such germs. Singularities and nontrivial monodromy may obstruct a single-valued global continuation even when continuation is possible along every short segment.

## References

1. Otto Forster, *Lectures on Riemann Surfaces*, Springer, 1981. [Publisher record](https://doi.org/10.1007/978-1-4612-5961-9). Relevant: Chapter 1, §§5–7.
