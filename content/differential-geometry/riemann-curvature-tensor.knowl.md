+++
id = "differential-geometry/riemann-curvature-tensor"
title = "Riemann curvature tensor"
kind = "definition"
summary = "The Riemann curvature tensor measures the failure of Levi–Civita covariant derivatives to commute."
aliases = ["Riemannian curvature tensor", "Riemann tensor"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \((M,g)\) be a [[differential-geometry/riemannian-manifold|Riemannian manifold]] with [[fiber-bundles/levicivita-connection-connection|Levi–Civita connection]] \(\nabla\). Its **Riemann curvature tensor** is the \((1,3)\)-tensor
\[
R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z
\]
for smooth [[fiber-bundles/vector-field|vector fields]] \(X,Y,Z\). The metric-lowered version is the \((0,4)\)-tensor
\[
\operatorname{Rm}(X,Y,Z,W)=g(R(X,Y)Z,W).
\]
The bracket correction makes \(R\) linear over smooth functions in all three arguments, so its value at a point depends only on the tangent vectors there. This convention fixes the overall sign of both tensors.

## Algebraic symmetries

For the convention in the core, the lowered tensor satisfies
\[
\operatorname{Rm}(X,Y,Z,W)=-\operatorname{Rm}(Y,X,Z,W)
=-\operatorname{Rm}(X,Y,W,Z)
\]
and
\[
\operatorname{Rm}(X,Y,Z,W)=\operatorname{Rm}(Z,W,X,Y).
\]
It also obeys the first [[fiber-bundles/bianchi-identity|Bianchi identity]]: the cyclic sum of \(R(X,Y)Z\) over \(X,Y,Z\) vanishes. These identities depend on both metric compatibility and vanishing torsion of the Levi–Civita connection; see [Lee, Chapter 7, “Curvature”](https://doi.org/10.1007/978-3-319-91755-9).

## Geometric information

For a two-plane spanned by linearly independent \(u,v\), the sectional curvature is
\[
K(u,v)=\frac{\operatorname{Rm}(u,v,v,u)}
{g(u,u)g(v,v)-g(u,v)^2}.
\]
Contractions of \(\operatorname{Rm}\) produce the [[differential-geometry/ricci-curvature|Ricci tensor]] and scalar curvature. Thus the Riemann tensor contains all sectional curvatures, while its contractions retain progressively less directional information.

Parallel transport around a small loop differs from the identity to first order in the enclosed area by the curvature operator. This gives the tensor its interpretation as infinitesimal holonomy.

## Examples and non-examples

[[linear-algebra/euclidean-space|Euclidean space]] with its standard metric has \(R=0\). The unit round sphere has constant positive sectional curvature, whereas hyperbolic space has constant negative sectional curvature.

A connection on an arbitrary [[fiber-bundles/vector-bundle|vector bundle]] also has [[fiber-bundles/curvature-of-a-vector-bundle-connection|curvature]], but that endomorphism-valued \(2\)-form is called the Riemann curvature tensor only when the connection is the Levi–Civita connection on \(TM\). A nonzero Christoffel symbol is not by itself curvature; such symbols can be nonzero in curvilinear coordinates on flat Euclidean space.

## Conventions and scope

**Warning.** Many authors define \(R(X,Y)Z\) with the opposite overall sign or permute the slots of the lowered tensor. Curvature formulas and the sign assigned to a round sphere must be read with the author’s convention. The displayed definition, not the name alone, determines the signs here.

## References

1. John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed., Graduate Texts in Mathematics 176, Springer, 2018. [Publisher record](https://doi.org/10.1007/978-3-319-91755-9). Relevant: Chapter 7, “Curvature.”
