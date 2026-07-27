+++
id = "fiber-bundles/quotient-vector-bundle"
title = "Quotient vector bundle"
kind = "definition"
summary = "The vector bundle whose fibers are the quotients of a vector bundle by a smooth vector subbundle."
aliases = ["vector bundle quotient"]
domains = ["fiber-bundles"]
section_mode = "progressive"
+++

Let \(E\to M\) be a smooth [[fiber-bundles/vector-bundle|vector bundle]] and let \(F\subseteq E\) be a smooth [[fiber-bundles/vector-subbundle|vector subbundle]]. The **quotient vector bundle** \(E/F\to M\) has fiber
\[
(E/F)_x=E_x/F_x.
\]
Its total space is the quotient of \(E\) by the equivalence relation \(v\sim w\) when \(v,w\in E_x\) and \(v-w\in F_x\). Local bundle frames adapted to \(F\) identify \(E/F\) with \(U\times\mathbb F^{r-k}\), and these charts give it a unique smooth vector-bundle structure for which the canonical map \(q:E\to E/F\) is a smooth, fiberwise-surjective [[fiber-bundles/vector-bundle-morphism|vector bundle morphism]] with kernel \(F\).

## Local construction

Choose a local frame \(e_1,\ldots,e_r\) of \(E\) such that \(e_1,\ldots,e_k\) frame \(F\). Then the residue classes of \(e_{k+1},\ldots,e_r\) form a local frame of \(E/F\). Consequently,
\[
\operatorname{rank}(E/F)=\operatorname{rank}(E)-\operatorname{rank}(F).
\]
Changes between adapted frames descend to invertible changes of quotient frames, so the construction is independent of the chosen frames.

## Exact sequence and splittings

The quotient projection fits into the [[fiber-bundles/short-exact-sequence-of-vector-bundles|short exact sequence]]
\[
0\longrightarrow F\longrightarrow E\overset{q}{\longrightarrow}E/F\longrightarrow0.
\]
After choosing a [[fiber-bundles/bundle-metric|bundle metric]], the orthogonal complement \(F^\perp\) maps isomorphically onto \(E/F\). This gives a smooth splitting on the usual paracompact smooth-manifold bases, but it depends on the metric and is not canonical. The quotient itself requires no such choice.

## Functoriality and examples

For a [[fiber-bundles/smooth-map|smooth map]] \(f:N\to M\), pullback preserves the quotient construction:
\[
f^*(E/F)\cong f^*E/f^*F.
\]
If \(N\subseteq M\) is an [[differential-geometry/embedded-submanifold|embedded submanifold]], its [[differential-geometry/normal-bundle|normal bundle]] is the quotient \(TM|_N/TN\). More generally, the cokernel of an injective constant-rank bundle morphism is a quotient vector bundle.

## References

1. D. Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: Chapter 3, subbundles, quotient bundles, and exact sequences.
2. L. W. Tu, *Differential Geometry: Connections, Curvature, and Characteristic Classes*, Springer, 2017. [DOI record](https://doi.org/10.1007/978-3-319-55092-8). Relevant: Chapter 1, operations on vector bundles.
