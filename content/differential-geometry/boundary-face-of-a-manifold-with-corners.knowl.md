+++
id = "differential-geometry/boundary-face-of-a-manifold-with-corners"
title = "Boundary face of a manifold with corners"
kind = "definition"
summary = "A globally chosen connected boundary hypersurface obtained by continuing one local boundary component through a manifold with corners."
aliases = ["face of a manifold with corners"]
domains = ["differential-geometry"]
prerequisites = ["differential-geometry/manifold-with-corners", "topology/connected-component"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

Let \(X\) be a [[differential-geometry/manifold-with-corners|manifold with corners]]. At \(x\in X\), a **local boundary component** is the germ at \(x\) of one of the coordinate hypersurfaces \(u_i=0\) in a corner chart for which \(u_i(x)=0\). The abstract boundary \(\partial X\) consists of pairs \((x,\beta)\), where \(\beta\) is such a local component. A **boundary face** is a [[topology/connected-component|connected component]] of \(\partial X\); its image in \(X\) is the closure of the corresponding connected depth-one piece. This definition retains which hypersurface is chosen when several meet at a corner.

## Incidence at corners

If \(x\) has depth \(r\), exactly \(r\) local boundary components lie over it. Thus the natural map \(\partial X\to X\) need not be injective: a corner point appears once for each incident face. Iterating the abstract-boundary construction records ordered choices of several incident hypersurfaces and refines the [[differential-geometry/corner-stratification|corner stratification]].

## Examples

For a square, the four closed edges are boundary faces, and each vertex has two preimages in the abstract boundary, one for each incident edge. For a disk, the boundary is one face. Merely taking the set-theoretic subset \(\{x:\operatorname{depth}(x)>0\}\) loses the multiplicity at a square’s vertices and therefore does not encode the same incidence data.

## Conventions and scope

**Warning.** “Face” is not standardized. Some authors call the image of a component of \(\partial X\) a boundary hypersurface, reserve “face” for intersections of such hypersurfaces, or require each face to be embedded. The abstract-boundary convention used here follows Joyce; statements using Melrose’s manifolds with faces may impose additional global embeddedness conditions.

## References

1. Dominic Joyce, “On Manifolds with Corners,” in *Advances in Geometric Analysis*, Advanced Lectures in Mathematics 21, International Press, 2012. [Author preprint](https://arxiv.org/abs/0910.3518). Relevant: §2, Definitions 2.5–2.8 and Remark 2.11, local boundary components, abstract boundaries, and corner spaces.
2. Richard B. Melrose, *Differential Analysis on Manifolds with Corners*, unfinished book manuscript. [Author-hosted manuscript](https://math.mit.edu/~rbm/book.html). Relevant: Chapter 1, boundary hypersurfaces and manifolds with faces.
