+++
id = "differential-geometry/critical-point-of-a-smooth-map"
title = "Critical point of a smooth map"
kind = "definition"
summary = "A point where the differential of a smooth map is not surjective onto the target tangent space."
aliases = ["critical point on a manifold"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(f:M\to N\) be a [[fiber-bundles/smooth-map|smooth map]] of finite-dimensional [[fiber-bundles/smooth-manifold|smooth manifolds]]. A point \(p\in M\) is a **critical point of \(f\)** if the [[fiber-bundles/differential-of-a-smooth-map|differential]]
\[
df_p:T_pM\longrightarrow T_{f(p)}N
\]
is not surjective. Equivalently, \(p\) is critical when the [[differential-geometry/rank-of-a-smooth-map|rank of \(f\) at \(p\)]] is strictly less than \(\dim N\). A point at which \(df_p\) is surjective is a **regular point**. This definition is intrinsic: coordinate changes multiply a Jacobian on the left and right by invertible matrices, so they do not change its rank or surjectivity.

## Scalar-valued maps

For \(f:M\to\mathbb R\), the target is one-dimensional, so \(p\) is critical exactly when \(df_p=0\). In local coordinates this means that all first [[real-analysis/partial-derivative|partial derivatives]] vanish. After choosing a Riemannian metric, the same condition can be written \(\operatorname{grad}f(p)=0\), but the metric and gradient are not needed for the definition.

## Dimension and examples

If \(\dim M<\dim N\), no differential \(T_pM\to T_{f(p)}N\) can be surjective, so every point is critical under this convention. For \(f:\mathbb R^2\to\mathbb R\), \(f(x,y)=x^2+y^2\), only the origin is critical. For the projection \(M\times F\to M\), every point is regular because the differential is surjective.

## Conventions and scope

“Singular point” is often used synonymously with critical point. In immersion theory, however, an author may instead call a point singular when \(df_p\) fails to be injective. The convention here is the one used for [[fiber-bundles/regular-value|regular values]] and [[differential-geometry/sards-theorem|Sard's theorem]]: critical means failure of surjectivity.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [DOI record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: chapters on submersions, regular points, and Sard's theorem.
2. Victor Guillemin and Alan Pollack, *Differential Topology*, AMS Chelsea Publishing, 2010 reprint. [DOI record](https://doi.org/10.1090/chel/370). Relevant: Chapter 1, critical points and regular values.
