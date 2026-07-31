+++
id = "differential-geometry/boundary-chart"
title = "Boundary chart"
kind = "definition"
summary = "A boundary chart gives local coordinates on a manifold with boundary in a relatively open subset of a Euclidean half-space."
aliases = ["half-space chart", "boundary coordinate chart"]
domains = ["differential-geometry"]
section_mode = "progressive"
+++

Let \(M\) be an \(n\)-dimensional [[differential-geometry/manifold-with-boundary|smooth manifold with boundary]], and write
\[
\mathbb H^n=\{(x^1,\ldots,x^n)\in\mathbb R^n:x^n\geq 0\}.
\]
A **boundary chart** on \(M\) is a pair \((U,\varphi)\) in its [[fiber-bundles/smooth-atlas|smooth atlas]] for which \(U\subseteq M\) is open and \(\varphi:U\to V\) is a homeomorphism onto a relatively open subset \(V\subseteq\mathbb H^n\). Its transition maps with overlapping boundary charts extend smoothly to maps between open subsets of \(\mathbb R^n\). It is centered at \(p\) when \(p\in U\); points represented on \(\partial\mathbb H^n\) are the boundary points of \(M\).

## Why relative openness matters

A neighborhood of a point on \(\partial\mathbb H^n\) is not open in \(\mathbb R^n\), but it is open in the [[topology/subspace-topology|subspace topology]] of \(\mathbb H^n\). Requiring relative openness therefore gives boundary points genuine manifold neighborhoods while retaining ordinary Euclidean neighborhoods at points with \(x^n>0\). Smoothness is tested by extensions to Euclidean-open sets because ordinary derivatives are not intrinsically defined on a one-sided domain. This is the half-space chart convention used in [Lee, Chapter 1, “Smooth Manifolds”].

## Basic consequences

The topological invariance of the half-space boundary implies that if one boundary chart sends \(p\) to \(x^n=0\), then every overlapping boundary chart does. Thus the distinction between [[differential-geometry/boundary-and-interior-of-a-manifold|boundary and interior points]] does not depend on coordinates.

At an interior point, restricting \(V\) to \(x^n>0\) turns a boundary chart into an ordinary [[fiber-bundles/smooth-chart|smooth chart]]. Near a boundary point, the first \(n-1\) coordinates restrict to coordinates on \(\partial M\), while \(x^n\) is an inward half-space coordinate.

## Examples and non-examples

The identity map from \(\mathbb H^n\) to itself is the standard boundary chart. A hemisphere of the sphere cut out by a closed half-space admits boundary charts obtained by flattening its equator.

The map from a neighborhood of \(0\) in \([0,\infty)\) onto an interval \((-\varepsilon,\varepsilon)\) is not a boundary chart: its image uses a full Euclidean neighborhood rather than a relatively open half-space neighborhood compatible with the one-sided local topology.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Graduate Texts in Mathematics 218, Springer, 2012. [Publisher record]. Relevant: Chapter 1, “Smooth Manifolds,” especially smooth manifolds with boundary.
