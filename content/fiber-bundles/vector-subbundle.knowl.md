+++
id = "fiber-bundles/vector-subbundle"
title = "Vector subbundle"
kind = "definition"
summary = "A smoothly varying family of linear subspaces inside the fibers of a vector bundle."
aliases = ["smooth vector subbundle", "subbundle of a vector bundle"]
domains = ["fiber-bundles"]
prerequisites = ["fiber-bundles/vector-bundle", "convex-analysis/linear-subspace", "fiber-bundles/local-trivialization", "fiber-bundles/smooth-embedding"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(E\to M\) be a smooth [[fiber-bundles/vector-bundle|vector bundle]]. A **vector subbundle of rank \(k\)** is a subset \(F\subseteq E\) such that \(F_x=F\cap E_x\) is a \(k\)-dimensional [[convex-analysis/linear-subspace|linear subspace]] of every fiber and, near each \(x\in M\), there is a [[fiber-bundles/local-trivialization|vector-bundle trivialization]]
\[
E|_U\cong U\times\mathbb F^r
\]
that carries \(F|_U\) onto \(U\times\mathbb F^k\) for a fixed coordinate subspace \(\mathbb F^k\subseteq\mathbb F^r\). These local models give \(F\to M\) a unique smooth vector-bundle structure for which the inclusion \(F\hookrightarrow E\) is a [[fiber-bundles/smooth-embedding|smooth embedding]] and is fiberwise linear.

## Local criteria

The following conditions are equivalent for a family of \(k\)-dimensional subspaces \(F_x\subseteq E_x\):

- \(F=\bigcup_xF_x\) is a rank-\(k\) vector subbundle;
- near every point there are [[fiber-bundles/section-of-a-fiber-bundle|smooth sections]] \(s_1,\ldots,s_k\) of \(E\) whose values form a basis of \(F_x\);
- locally, \(F\) is the image of a smooth field of projections of constant rank \(k\).

The constant-dimension requirement is essential. A family of linear subspaces whose dimension jumps is generally not a vector bundle.

## Kernels and images

Let \(\Phi:E\to E'\) be a [[fiber-bundles/bundle-map|smooth vector-bundle map]] over the identity of \(M\). If the fiberwise rank of \(\Phi\) is locally constant, then
\[
\ker\Phi=\bigcup_{x\in M}\ker\Phi_x
\quad\text{and}\quad
\operatorname{im}\Phi=\bigcup_{x\in M}\operatorname{im}\Phi_x
\]
are vector subbundles of \(E\) and \(E'\), respectively. Without constant rank, these sets need not be subbundles even though each individual fiber is a linear subspace.

## Examples

- The [[fiber-bundles/tangent-bundle|tangent bundle]] of an [[differential-geometry/embedded-submanifold|embedded submanifold]] \(N\subseteq M\) is a subbundle \(TN\subseteq TM|_N\).
- A smooth distribution of constant rank is a vector subbundle of \(TM\); integrability is an additional condition and is not part of the definition.
- For a smooth [[fiber-bundles/bundle-metric|bundle metric]], the [[linear-algebra/orthogonal-complement|orthogonal complement]] \(F^\perp\) of a vector subbundle \(F\subseteq E\) is another vector subbundle, and \(E=F\oplus F^\perp\).
- The [[fiber-bundles/vertical-subbundle|vertical]] and [[fiber-bundles/horizontal-subbundle|horizontal]] distributions associated with a bundle and a connection are standard subbundles.

## References

1. Dale Husemoller, *Fibre Bundles*, 3rd ed., Springer, 1994. [DOI record](https://doi.org/10.1007/978-1-4757-2261-1). Relevant: vector bundles and subbundles.
2. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2013. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: vector bundles and constant-rank constructions.
