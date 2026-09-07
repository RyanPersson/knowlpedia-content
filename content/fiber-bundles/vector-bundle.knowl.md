+++
id = "fiber-bundles/vector-bundle"
title = "Vector bundle"
kind = "knowl"
summary = "A smooth fiber bundle whose fibers are vector spaces and whose local trivializations are fiberwise linear."
aliases = ["vector-bundle", "Vector bundle"]
domains = ["fiber-bundles"]
legacy_source_path = "fiber-bundles/vector-bundle.md"
prerequisites = ["fiber-bundles/smooth-manifold", "fiber-bundles/smooth-fiber-bundle", "linear-algebra/vector-space", "linear-algebra/linear-map", "convex-analysis/basis-hamel-basis-and-dimension"]
dependency_heuristic = "semantic-curriculum-review-v1"
dependency_review_count = 3
+++

A **smooth \(\mathbb K\)-vector bundle** of rank \(k\), for \(\mathbb K\in\{\mathbb R,\mathbb C\}\), over a [[fiber-bundles/smooth-manifold|smooth manifold]] \(M\) is a [[fiber-bundles/smooth-fiber-bundle|smooth fiber bundle]] \(\pi:E\to M\) together with the structure of a \(k\)-dimensional \(\mathbb K\)-vector space on each fiber \(E_x=\pi^{-1}(x)\), such that:

- the [[fiber-bundles/typical-fiber|typical fiber]] is \(\mathbb K^k\), and
- there exists an open cover \(\{U_i\}\) of \(M\) with [[fiber-bundles/local-trivialization|local trivializations]] \(\Phi_i:\pi^{-1}(U_i)\to U_i\times\mathbb K^k\) whose restrictions \(\Phi_i|_{E_x}:E_x\to \mathbb K^k\) are linear isomorphisms for each \(x\in U_i\).

## Equivalent characterizations
Equivalently, the [[fiber-bundles/transition-function|transition functions]] of such a bundle take values in \(\mathrm{GL}(k,\mathbb K)\subset \mathrm{Diff}(\mathbb K^k)\). The [[fiber-bundles/tangent-bundle|tangent bundle]] and [[fiber-bundles/cotangent-bundle|cotangent bundle]] are the fundamental real examples; many constructions in differential geometry (e.g. a [[fiber-bundles/connection-on-a-vector-bundle|connection on a vector bundle]]) are formulated for vector bundles.

## Examples
1. **Trivial rank-\(k\) bundle:** \(M\times \mathbb{R}^k\to M\) is a vector bundle with the obvious fiberwise linear structure.
2. **Tangent and cotangent bundles:** for an \(n\)-manifold \(M\), \(TM\to M\) and \(T^*M\to M\) are rank-\(n\) vector bundles.
3. **Möbius [[fiber-bundles/line-bundle|line bundle]]:** a nontrivial rank-1 real vector bundle over \(S^1\) with transition function \(-1\) on the overlap of two arcs.
