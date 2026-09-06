+++
id = "topology/fundamental-class"
title = "Fundamental class"
kind = "definition"
summary = "The top-dimensional homology class determined by an orientation of a closed manifold."
aliases = ["orientation class", "fundamental homology class"]
domains = ["topology", "fiber-bundles"]
section_mode = "progressive"
prerequisites = ["topology/closed-manifold", "fiber-bundles/smooth-manifold", "fiber-bundles/orientation-of-a-real-vector-bundle"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(M\) be a connected [[topology/closed-manifold|closed \(n\)-manifold]] with an orientation over a commutative coefficient ring \(R\). A **fundamental class** is the unique class
\[
[M]\in H_n(M;R)
\]
whose image under
\[
H_n(M;R)\longrightarrow H_n(M,M\setminus\{x\};R)
\]
is the local orientation generator at every \(x\in M\). Thus \([M]\) is the global homology class that consistently assembles all local choices of orientation. For a [[fiber-bundles/smooth-manifold|smooth manifold]], an [[fiber-bundles/orientation-of-a-real-vector-bundle|orientation of the tangent bundle]] determines the corresponding integral fundamental class.

## Existence and variants

A connected closed manifold has an integral fundamental class exactly when it is orientable. Every closed manifold has a canonical mod-\(2\) fundamental class. If \(M\) has boundary, the oriented class lies instead in \(H_n(M,\partial M;R)\); if \(M\) is noncompact, the corresponding object belongs to locally finite homology. These variants preserve the same local-generator condition.

## Pairings and consequences

The evaluation pairing sends a top-degree cohomology class \(a\) to
\[
\langle a,[M]\rangle\in R.
\]
Cap product with \([M]\) is the map underlying Poincaré duality. Products of [[fiber-bundles/characteristic-class|characteristic classes]] evaluated in this way produce [[fiber-bundles/characteristic-number|characteristic numbers]], while the Euler class of \(TM\) evaluates to the Euler characteristic under the usual hypotheses.

## Examples and orientation dependence

The standard orientation of \(S^n\) selects one of the two generators of \(H_n(S^n;\mathbb Z)\cong\mathbb Z\). Reversing the orientation replaces \([M]\) by \(-[M]\). For a closed nonorientable manifold, no integral class satisfies the local-generator condition, although its mod-\(2\) fundamental class still exists.

## References

1. Allen Hatcher, *Algebraic Topology*, Cambridge University Press, 2002. [Author-hosted book record](https://pi.math.cornell.edu/~hatcher/AT/ATpage.html). Relevant: §3.3, orientations, fundamental classes, and Poincaré duality.
