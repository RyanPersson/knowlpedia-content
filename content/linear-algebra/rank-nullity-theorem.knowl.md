+++
id = "linear-algebra/rank-nullity-theorem"
title = "Rank–nullity theorem"
kind = "knowl"
summary = "For a linear map on a finite-dimensional space, dimension equals rank plus nullity."
aliases = ["rank-nullity-theorem", "Rank–nullity theorem"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/rank-nullity-theorem.md"
prerequisites = ["linear-algebra/linear-map", "convex-analysis/image-and-kernel-linear-isomorphism", "convex-analysis/basis-hamel-basis-and-dimension"]
dependency_heuristic = "semantic-curriculum-review-v1"
dependency_review_count = 1
+++

**Rank–nullity theorem:** Let \(T:V\to W\) be a [[linear-algebra/linear-map|linear map]] between finite-dimensional [[linear-algebra/vector-space|vector spaces]]. Define
\[
\begin{gathered}
\ker T=\{v\in V:T(v)=0\},\\
\operatorname{im}T=\{T(v):v\in V\}.
\end{gathered}
\]
Then
\[
\dim V=\dim(\ker T)+\dim(\operatorname{im}T).
\]
## Rank and nullity

In particular, the rank \(\operatorname{rank}(T)=\dim(\operatorname{im}T)\) and the nullity \(\operatorname{nullity}(T)=\dim(\ker T)\) satisfy \(\dim V=\operatorname{rank}(T)+\operatorname{nullity}(T)\).

## Remarks

The set \(\operatorname{im}T\) is the [[shared-foundations/image|image]] of the underlying function, and \(\ker T\) is the [[shared-foundations/preimage|preimage]] of \(\{0\}\). This identity is the basic dimension bookkeeping behind the structure of solution spaces to linear equations.
