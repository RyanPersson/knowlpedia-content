+++
id = "differential-geometry/real-projective-space"
title = "Real projective space"
kind = "definition"
summary = "The smooth manifold of real lines through the origin in real Euclidean space."
aliases = ["RPn", "real projective n-space", "real projective manifold"]
domains = ["differential-geometry", "algebraic-geometry-foundations", "topology"]
prerequisites = ["convex-analysis/linear-subspace", "algebraic-geometry-foundations/projective-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

For \(n\ge0\), **real projective \(n\)-space** is the set of one-dimensional real [[convex-analysis/linear-subspace|linear subspaces]] of \(\mathbb R^{n+1}\):
\[
\mathbb{RP}^n=\mathbb P(\mathbb R^{n+1}).
\]
The standard affine charts of [[algebraic-geometry-foundations/projective-space|projective space]] give it the structure of a smooth manifold of real dimension \(n\).

## Quotient descriptions

Every real line contains exactly two unit vectors, so normalization gives a diffeomorphism
\[
\mathbb{RP}^n\cong S^n/\{x\sim -x\}.
\]
Equivalently,
\[
\mathbb{RP}^n\cong
(\mathbb R^{n+1}\setminus\{0\})/\mathbb R^\times.
\]
The sphere map \(S^n\to\mathbb{RP}^n\) is a two-sheeted covering for \(n\ge1\). These quotient descriptions show that \(\mathbb{RP}^n\) is compact and connected for \(n\ge1\).

## Homogeneous-space descriptions

The [[lie-groups/orthogonal-group|orthogonal group]] acts transitively on real lines, and the stabilizer of the first coordinate line is \(O(1)\times O(n)\). Hence
\[
\mathbb{RP}^n\cong O(n+1)/(O(1)\times O(n))
\]
as a [[lie-groups/homogeneous-space|homogeneous space]]. The [[algebra-groups/projective-general-linear-group|projective general linear group]] \(\operatorname{PGL}_{n+1}(\mathbb R)\) also acts transitively; the stabilizer of a line is a projective parabolic subgroup.

## Geometry and topology

The case \(\mathbb{RP}^1\) is diffeomorphic to a circle. For \(n\ge2\), the sphere covering is universal and
\(\pi_1(\mathbb{RP}^n)\cong\mathbb Z/2\). For \(n\ge1\), \(\mathbb{RP}^n\) is orientable exactly when \(n\) is odd.

## References

1. John M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer, 2012. [Publisher record](https://doi.org/10.1007/978-1-4419-9982-5). Relevant: quotient manifolds, projective spaces, and covering maps.
2. John W. Milnor and James D. Stasheff, *Characteristic Classes*, Princeton University Press, 1974. [Publisher record](https://doi.org/10.1515/9781400881826). Relevant: §§4–5, real projective spaces and tautological bundles.
