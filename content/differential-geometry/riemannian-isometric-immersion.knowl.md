+++
id = "differential-geometry/riemannian-isometric-immersion"
title = "Riemannian isometric immersion"
kind = "definition"
summary = "A smooth map whose pullback of the target Riemannian metric is the source metric."
aliases = ["isometric immersion", "Riemannian immersion"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \((M,g_M)\) and \((N,g_N)\) be [[differential-geometry/riemannian-manifold|Riemannian manifolds]]. A **Riemannian isometric immersion** is a smooth map \(f:M\to N\) such that
\[
f^*g_N=g_M.
\]
Pointwise, this means
\[
g_N(df_pu,df_pv)=g_M(u,v)
\]
for all \(p\in M\) and \(u,v\in T_pM\). Positive-definiteness implies that \(df_p\) is injective, so the pullback equation already forces \(f\) to be a [[fiber-bundles/smooth-immersion|smooth immersion]].

The adjective “isometric” here refers to the Riemannian tensors. It does not by itself assert that \(f\) is injective as a map, an embedding, or distance-preserving for the global geodesic distance between arbitrary points.

## Special cases

If \(f\) is also a smooth embedding, it is an **isometric embedding**. If it is a diffeomorphism, it is a **Riemannian isometry**, and the pullback equation implies that its inverse is also an isometry. Thus isometric immersions compose, while Riemannian isometries are the isomorphisms among them.

The inclusion of a Riemannian submanifold equipped with the induced metric is an isometric immersion. A covering map equipped with the pulled-back metric is another example that need not be injective.

## Added structures

For Hermitian or Kähler manifolds, a Riemannian isometric immersion need not preserve the complex structures. Adding the equation
\[
df\circ J_M=J_N\circ df
\]
gives a [[differential-geometry/holomorphic-isometric-immersion|holomorphic isometric immersion]], which preserves both the metrics and the associated fundamental two-forms.

## References

1. John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed., Springer, 2018. [DOI record](https://doi.org/10.1007/978-3-319-91755-9). Relevant: Riemannian submanifolds, isometric immersions, and isometries.
2. Manfredo P. do Carmo, *Riemannian Geometry*, Birkhäuser, 1992. [DOI record](https://doi.org/10.1007/978-1-4757-2201-7). Relevant: isometric immersions and induced metrics.
