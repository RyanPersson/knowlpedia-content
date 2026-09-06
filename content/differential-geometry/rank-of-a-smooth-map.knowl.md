+++
id = "differential-geometry/rank-of-a-smooth-map"
title = "Rank of a smooth map"
kind = "definition"
summary = "The dimension of the image of a smooth map's differential at a specified point."
aliases = ["rank of the differential", "rank at a point"]
domains = ["differential-geometry"]
prerequisites = ["fiber-bundles/smooth-map", "fiber-bundles/differential-of-a-smooth-map", "linear-algebra/linear-map"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(f:M\to N\) be a [[fiber-bundles/smooth-map|smooth map]] and let \(p\in M\). The **rank of \(f\) at \(p\)** is the rank of its [[fiber-bundles/differential-of-a-smooth-map|differential]]
\[
df_p:T_pM\longrightarrow T_{f(p)}N;
\qquad
\operatorname{rank}_p(f)=\dim(\operatorname{im}df_p).
\]
Thus \(0\leq \operatorname{rank}_p(f)\leq\min(\dim M,\dim N)\). The map \(f\) has **constant rank \(r\)** on a subset if \(\operatorname{rank}_p(f)=r\) at every point of that subset. The definition is independent of coordinates because changing charts composes the coordinate Jacobian with invertible [[linear-algebra/linear-map|linear maps]].

## Full-rank cases

If \(\operatorname{rank}_p(f)=\dim M\), then \(df_p\) is injective; \(f\) is an [[fiber-bundles/smooth-immersion|immersion]] at \(p\). If \(\operatorname{rank}_p(f)=\dim N\), then \(df_p\) is surjective; \(f\) is a [[fiber-bundles/smooth-submersion|submersion]] at \(p\). When the dimensions agree, either condition says that \(df_p\) is an isomorphism, and the [[shared-foundations/inverse-function|inverse function]] theorem makes \(f\) a [[algebraic-geometry-foundations/local-diffeomorphism|local diffeomorphism]] near \(p\).

## Constant-rank normal form

If the rank is constantly \(r\) on a neighborhood of \(p\), the constant-rank theorem gives local coordinates centered at \(p\) and \(f(p)\) in which
\[
(x^1,\ldots,x^m)\longmapsto(x^1,\ldots,x^r,0,\ldots,0).
\]
This normal form explains both the image dimension \(r\) and the local fiber dimension \(m-r\). It is a theorem requiring local constancy of rank, not an alternative definition of the rank at a single point.

## Semicontinuity and conventions

The rank function \(p\mapsto\operatorname{rank}_p(f)\) is lower semicontinuous: the set where the rank is at least \(r\) is open, since some \(r\times r\) Jacobian minor remains nonzero nearby. Consequently the maximal-rank locus is open, but lower-rank loci may be singular. The [[linear-algebra/rank-nullity-theorem|rank–nullity theorem]] gives \(\dim\ker df_p=\dim M-\operatorname{rank}_p(f)\). “Rank of \(f\)” without a point should be used only when the rank is constant or when a stated convention means the maximum rank.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Graduate Texts in Mathematics 218, Springer, 2012. [Publisher record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: Chapter 4, rank, immersion, submersion, and constant-rank theorems.
2. Morris W. Hirsch, *Differential Topology*, Graduate Texts in Mathematics 33, Springer, 1976. [Publisher record](https://doi.org/10.1007/978-1-4684-9449-5). Relevant: Chapter 1, rank and local normal forms.
