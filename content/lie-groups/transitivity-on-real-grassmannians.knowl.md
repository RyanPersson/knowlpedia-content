+++
id = "lie-groups/transitivity-on-real-grassmannians"
title = "Transitivity on real Grassmannians"
kind = "theorem"
summary = "The orthogonal and special orthogonal groups act transitively on real Grassmannians, with stabilizers determined by block orthogonal groups."
aliases = ["orthogonal transitivity on the Grassmannian", "real Grassmannian homogeneous space", "SO(n) action on Gr(k,n)"]
domains = ["lie-groups", "differential-geometry"]
prerequisites = ["lie-groups/orthogonal-group", "differential-geometry/grassmannian", "lie-groups/special-orthogonal-group"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

For \(0\leq k\leq n\), the natural action of
[[lie-groups/orthogonal-group|\(O(n)\)]] on the
[[differential-geometry/grassmannian|real Grassmannian]]
\(\operatorname{Gr}_k(\mathbb R^n)\) is transitive. For the coordinate plane
\(E=\mathbb R^k\oplus0\), its stabilizer is \(O(k)\times O(n-k)\), so

\[
\operatorname{Gr}_k(\mathbb R^n)
\cong O(n)/(O(k)\times O(n-k)).
\]

For \(0<k<n\), [[lie-groups/special-orthogonal-group|\(SO(n)\)]] is also
transitive, but its full stabilizer of the **unoriented** plane \(E\) is

\[
S(O(k)\times O(n-k))
=\{(A,B):\det(A)\det(B)=1\}.
\]

Consequently,

\[
\operatorname{Gr}_k(\mathbb R^n)
\cong SO(n)/S(O(k)\times O(n-k)).
\]

## Proof mechanism

Given \(k\)-planes \(W,W'\), choose [[linear-algebra/orthonormal-basis|orthonormal bases]] of them and of their
[[linear-algebra/orthogonal-complement|orthogonal complements]]. The linear map carrying the first combined basis to
the second is orthogonal and sends \(W\) to \(W'\). If its determinant is
\(-1\) and \(0<k<n\), composing with a reflection that preserves \(W'\)
setwise changes the determinant without changing the image plane. This gives
an element of \(SO(n)\).

An orthogonal transformation stabilizes \(E\) exactly when it also stabilizes
\(E^{\perp}\), hence is block diagonal with blocks in \(O(k)\) and
\(O(n-k)\). Intersecting this block group with \(SO(n)\) imposes the product
determinant condition above.

## Connected versus full stabilizers

For \(0<k<n\), the [[lie-groups/identity-component-of-a-lie-group|identity component]] of the \(SO(n)\)-stabilizer is

\[
SO(k)\times SO(n-k),
\]

where \(SO(1)\) is the trivial group. The full stabilizer is generally larger:
it also contains block pairs that reverse both the plane orientation and its
complement orientation. Thus \(SO(n)/(SO(k)\times SO(n-k))\) is not the
ordinary Grassmannian; it is the
[[differential-geometry/oriented-grassmannian|oriented Grassmannian]].

At \(k=0\) or \(k=n\), the Grassmannian is a point and its stabilizer is all of
the acting group. These boundary cases are excluded from the displayed
\(SO(n)\) stabilizer comparison.

## References

1. Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric
   Spaces*, American Mathematical Society, 2001. [Publisher record](https://doi.org/10.1090/gsm/034).
2. John W. Milnor and James D. Stasheff, *Characteristic Classes*, Princeton
   University Press, 1974, §§5–6. [Publisher record](https://doi.org/10.1515/9781400881826).
