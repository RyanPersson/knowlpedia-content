+++
id = "differential-geometry/corner-stratification"
title = "Corner stratification"
kind = "definition"
summary = "The corner stratification partitions a manifold with corners according to the number of vanishing local boundary coordinates."
aliases = ["depth stratification", "boundary strata of a manifold with corners"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/manifold-with-corners", "differential-geometry/depth-of-a-point-in-a-manifold-with-corners", "fiber-bundles/smooth-manifold"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(M\) be an \(n\)-dimensional
[[differential-geometry/manifold-with-corners|manifold with corners]]. Its
**corner stratification** is the partition
\[
M=\coprod_{r=0}^n S^r(M),\qquad
S^r(M)=\{x\in M:\operatorname{depth}_M(x)=r\},
\]
where [[differential-geometry/depth-of-a-point-in-a-manifold-with-corners|the depth of \(x\)]] is the number of vanishing boundary coordinates in any
corner chart at \(x\). Each \(S^r(M)\), with its induced smooth structure, is
an \((n-r)\)-dimensional [[fiber-bundles/smooth-manifold|smooth manifold]]
without boundary, possibly empty or disconnected. The depth-zero stratum is
the interior; positive-depth strata
record the open pieces where a fixed number of local boundary hypersurfaces
meet.

## Local model and incidence

In the orthant \([0,\infty)^k\times\mathbb R^{n-k}\), the depth-\(r\) stratum
is the union of loci obtained by setting exactly \(r\) of the first \(k\)
coordinates to zero and keeping the others positive. A limit of depth-\(r\)
points can have depth greater than \(r\), so
\[
\overline{S^r(M)}\subseteq\bigcup_{s\geq r}S^s(M).
\]
Equality need not hold globally when components or faces do not meet.

## Examples and products

For a square, the interior, open edges, and vertices are respectively the
depth-zero, depth-one, and depth-two strata. For manifolds with corners
\(M\) and \(N\), depths add on the
[[differential-geometry/product-manifold|product manifold]], so the
depth-\(r\) stratum of \(M\times N\) is the disjoint union of
\(S^i(M)\times S^j(N)\) over \(i+j=r\).

## Strata versus faces

**Warning.** A depth stratum does not label the local boundary hypersurfaces
that meet there. A [[topology/connected-component|connected component]] of \(S^r(M)\), a closed face, and an
iterated-boundary component are related but convention-dependent notions.

## References

1. Dominic Joyce, “On Manifolds with Corners,” final preprint version, 2010. [arXiv record](https://arxiv.org/abs/0910.3518). Relevant: §§2–3, depth, strata, boundaries, and corner functors.
2. Dominic Joyce, “A Generalization of Manifolds with Corners,” *Advances in Mathematics* 299 (2016), 760–862. [DOI record](https://doi.org/10.1016/j.aim.2016.06.004). Relevant: §2, ordinary corner stratifications used as the comparison case.
