+++
id = "formal-groups/formal-group"
title = "Formal group"
kind = "definition"
summary = "A group object in formal schemes; in finite-dimensional formal Lie theory its pointed formal scheme is a formal disc."
aliases = ["formal Lie group", "formal group scheme"]
domains = ["formal-groups", "algebraic-geometry-foundations"]
section_mode = "progressive"
prerequisites = ["algebra-category-theory/group-object", "algebraic-geometry-foundations/formal-scheme"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

A **formal group over a base \(S\)** is a
[[algebra-category-theory/group-object|group object]] in the category of
[[algebraic-geometry-foundations/formal-scheme|formal schemes]] over \(S\).
It consists of a formal scheme \(\mathcal G\) with multiplication, identity,
and inverse morphisms
\[
m:\mathcal G\times_S\mathcal G\to\mathcal G,\qquad
e:S\to\mathcal G,\qquad
i:\mathcal G\to\mathcal G,
\]
satisfying the associative, unit, and inverse diagrams. It is commutative when
\(m=m\circ\tau\), where \(\tau\) swaps the two factors.

## Finite-dimensional formal Lie groups

For the characteristic-zero Lie correspondence used here, \(S=\operatorname{Spec}k\)
for a field \(k\), and a **finite-dimensional formally smooth formal group**
means one whose pointed underlying formal scheme is isomorphic to a formal
disc
\[
(\mathcal G,e)\cong
\left(\operatorname{Spf}k[[X_1,\ldots,X_n]],0\right)
\]
for some finite \(n\). The isomorphism is not part of the coordinate-free
formal group; choosing one supplies coordinates.

Broader usages include commutative formal groups over general bases and formal
groups not represented by a finite-dimensional [[formal-groups/formal-affine-space|formal disc]]. Those objects are
not silently included in the finite-dimensional equivalence.

## Coordinates

After a coordinate choice, the pullback of multiplication is determined by
\[
m^*(X_i)=F_i(X,Y),
\]
and the group diagrams become the identities for a
[[formal-groups/formal-group-law|formal group law]]. Different coordinate
choices give isomorphic laws, so the formal group is the intrinsic object and
the law is a presentation.

## Tangent structure

The [[differential-geometry/tangent-space|tangent space]] at the identity carries a canonical [[fiber-bundles/lie-bracket|Lie bracket]], producing
the [[formal-groups/tangent-lie-algebra|tangent Lie algebra]]
\(\operatorname{Lie}(\mathcal G)\). In characteristic zero and within the
finite-dimensional formal-disc category, this construction is an equivalence
of categories, not merely an assignment of an invariant.

## References

1. Michiel Hazewinkel, *Formal Groups and Applications*, AMS Chelsea Publishing, 2012. [AMS book record](https://bookstore.ams.org/chel-375-h). Relevant: Chapters 2 and 7, multidimensional formal groups and bialgebras.
2. Jean-Pierre Serre, *Lie Algebras and Lie Groups*, second edition, Springer, 1992. [Publisher record](https://link.springer.com/book/10.1007/978-3-540-70634-2). Relevant: Part I, formal groups and Lie algebras.
