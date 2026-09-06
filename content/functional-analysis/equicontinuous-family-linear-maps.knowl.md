+++
id = "functional-analysis/equicontinuous-family-linear-maps"
title = "Equicontinuous family of continuous linear maps"
kind = "definition"
summary = "A family of continuous linear maps that satisfies one continuity estimate uniformly across all its members."
aliases = ["equicontinuous operator family", "equicontinuous set of functionals"]
domains = ["functional-analysis"]
prerequisites = ["functional-analysis/topological-vector-space", "functional-analysis/continuous-linear-map", "topology/neighborhood", "linear-algebra/linear-map"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(E\) and \(F\) be [[functional-analysis/topological-vector-space|topological vector spaces]], and let \(\mathcal T\) be a family of [[functional-analysis/continuous-linear-map|continuous linear maps]] \(T:E\to F\). The family \(\mathcal T\) is **equicontinuous** if, for every [[topology/neighborhood|neighborhood]] \(V\) of \(0\) in \(F\), there is a neighborhood \(U\) of \(0\) in \(E\) such that
\[
T(U)\subseteq V
\qquad\text{for every }T\in\mathcal T.
\]
The same source neighborhood must therefore control all operators in the family. For [[linear-algebra/linear-map|linear maps]], this condition at \(0\) is equivalent to equicontinuity at every point.

## Seminorm criterion

Suppose \(E\) and \(F\) are [[functional-analysis/locally-convex-space|locally convex]]. Equicontinuity is equivalent to the following: for every continuous [[convex-analysis/seminorm|seminorm]] \(q\) on \(F\), there are continuous seminorms \(p_1,\ldots,p_n\) on \(E\) and \(C>0\) such that
\[
q(Tx)\le C\max_{1\le j\le n}p_j(x)
\]
for all \(T\in\mathcal T\) and \(x\in E\). This is the locally convex analogue of a uniform operator-norm bound.

## Duality and uniform boundedness

For a family \(\mathcal T\) in the [[functional-analysis/topological-dual|topological dual]] \(E'\), equicontinuity means that some zero-neighborhood \(U\subseteq E\) satisfies \(\lvert\varphi(x)\rvert\le1\) for every \(\varphi\in\mathcal T\) and \(x\in U\); equivalently, \(\mathcal T\) lies in the polar of \(U\). If \(E\) is [[functional-analysis/barreled-space|barreled]], [[real-analysis/pointwise-bounded-family|pointwise bounded families]] of continuous linear maps from \(E\) into a locally convex space are equicontinuous.

## Stability and cautions

Subfamilies, finite unions, and the balanced [[convex-analysis/convex-hull|convex hull]] of an [[real-analysis/equicontinuous-family|equicontinuous family]] remain equicontinuous. Composing on either side with a fixed continuous linear map also preserves equicontinuity. Equicontinuity is stronger than requiring each member to be continuous. It is also distinct from equicontinuity of arbitrary maps between [[topology/metric-space|metric spaces]], although the two definitions agree for linear maps when translated into zero-neighborhood language.

## References

1. François Trèves, *Topological Vector Spaces, Distributions and Kernels*, Academic Press, 1967; Dover reprint, 2006. [Dover publisher record](https://store.doverpublications.com/products/9780486453521). Relevant: Chapter 32 on equicontinuity and uniform boundedness.
2. Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces*, 2nd ed., Springer, 1999. [Springer DOI record](https://doi.org/10.1007/978-1-4612-1468-7). Relevant: Chapter III on spaces of continuous linear mappings.
