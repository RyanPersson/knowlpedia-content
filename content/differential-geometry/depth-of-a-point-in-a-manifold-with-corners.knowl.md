+++
id = "differential-geometry/depth-of-a-point-in-a-manifold-with-corners"
title = "Depth of a point in a manifold with corners"
kind = "definition"
summary = "The number of local boundary coordinates that vanish at a point of a manifold with corners."
aliases = ["corner depth", "depth stratum"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(M\) be an \(n\)-dimensional [[differential-geometry/manifold-with-corners|manifold with corners]], and choose a corner chart in which \(x\in M\) corresponds to
\[
(u_1,\ldots,u_k,v_{k+1},\ldots,v_n)
\in[0,\infty)^k\times\mathbb R^{n-k}.
\]
The **depth** of \(x\) is
\[
\operatorname{depth}_M(x)=\#\{i\in\{1,\ldots,k\}:u_i=0\}.
\]
Compatibility of corner charts makes this number independent of the chosen chart. For \(0\leq r\leq n\), the depth-\(r\) stratum is
\[
S^r(M)=\{x\in M:\operatorname{depth}_M(x)=r\}.
\]
Thus depth is intrinsic even though the individual boundary coordinates are not.
It measures local codimension in the canonical [[differential-geometry/corner-stratification|corner stratification]].

## Stratification

The decomposition
\[
M=\coprod_{r=0}^n S^r(M)
\]
is a stratification by smooth manifolds without boundary, with \(\dim S^r(M)=n-r\). The depth-zero stratum is the interior. The closure of \(S^r(M)\) is the union of strata of depth at least \(r\). These properties are formulated for ordinary corners in [Joyce, Definition 2.6](https://doi.org/10.1016/j.aim.2016.06.004).

## Examples and products

For the square \([0,1]^2\), interior points have depth zero, points in open edges have depth one, and vertices have depth two. On a [[differential-geometry/manifold-with-boundary|manifold with boundary]], only depths zero and one occur. In a product,
\[
\operatorname{depth}_{M\times N}(x,y)
=\operatorname{depth}_M(x)+\operatorname{depth}_N(y),
\]
because the vanishing coordinates from the two factors concatenate.

## Depth versus a chosen face

**Warning.** Depth counts how many local boundary hypersurfaces meet at a point; it does not choose or label those hypersurfaces. A theory of faces or an iterated boundary carries additional incidence data, and conventions for that data differ across treatments of manifolds with corners.

## References

1. Dominic Joyce, “A Generalization of Manifolds with Corners,” *Advances in Mathematics* 299 (2016), 760–862. [DOI record](https://doi.org/10.1016/j.aim.2016.06.004). Relevant: §2, Definition 2.6 for depth and depth strata of ordinary manifolds with corners, and §3.4 for the generalized construction.
2. Dominic Joyce, “On Manifolds with Corners,” final preprint version, 2010. [arXiv record](https://arxiv.org/abs/0910.3518). Relevant: §2, boundaries and corners.
