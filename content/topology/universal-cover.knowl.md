+++
id = "topology/universal-cover"
title = "Universal cover"
kind = "definition"
summary = "A connected simply connected covering space that covers a given base space."
aliases = ["universal covering space", "universal covering"]
domains = ["topology"]
section_mode = "progressive"
prerequisites = ["topology/covering-space", "topology/simply-connected-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Let \(X\) be a topological space. A **universal cover** of \(X\) is a [[topology/covering-space|covering map]]
\[
p:\widetilde X\to X
\]
such that \(\widetilde X\) is connected and [[topology/simply-connected-space|simply connected]]. Thus the total space is a connected simply connected space that covers \(X\).

## Existence and uniqueness

If \(X\) is connected, locally path-connected, and semilocally simply connected, then a universal cover exists. It is unique up to a homeomorphism over \(X\). In particular, every connected smooth manifold has a universal cover, since smooth manifolds satisfy these local hypotheses.

## Deck transformations

A deck transformation is a homeomorphism \(D:\widetilde X\to\widetilde X\) with \(p\circ D=p\). After choosing a basepoint in \(X\) and a lift, the deck transformation group of the universal cover is identified with the fundamental group \(\pi_1(X)\), up to the left/right action convention used for lifting paths. The basepoint choice changes this identification by the corresponding standard conjugacy ambiguity.

For a path-connected, locally path-connected, semilocally simply connected base, every connected covering is obtained from the universal cover by a subgroup of \(\pi_1(X)\), with the usual conjugacy ambiguity when no lifted basepoint is chosen.

## Examples

The identity map is the universal cover of a simply connected space. The exponential covering \(\mathbb R\to S^1\), \(t\mapsto e^{2\pi i t}\), is the universal cover of the circle; its deck group is isomorphic to \(\mathbb Z\).

## References

1. Allen Hatcher, *Algebraic Topology*, Cambridge University Press, 2002, Chapter 1, §1.3, “Covering Spaces,” especially pp. 60–73. [Author-hosted PDF](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf).
