+++
id = "formal-groups/coordinate-hopf-algebra"
title = "Coordinate Hopf algebra of an affine formal group"
kind = "definition"
summary = "The complete commutative topological Hopf algebra of functions on an affine formal group."
aliases = ["formal Hopf algebra", "complete coordinate Hopf algebra", "Hopf algebra of a formal group"]
domains = ["formal-groups", "algebra-coalgebras", "algebraic-geometry-foundations"]
prerequisites = ["formal-groups/formal-group", "topology/continuous-map", "algebra-coalgebras/hopf-algebra", "algebra-topological/completed-tensor-product"]
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(k\) be a commutative ring and let
\(G=\operatorname{Spf}(A)\) be an affine [[formal-groups/formal-group|formal
group]] over \(k\), where \(A\) is a complete separated commutative
topological \(k\)-algebra. Pullback along the multiplication, identity, and
inverse of \(G\) gives [[topology/continuous-map|continuous maps]]
\[
\Delta:A\longrightarrow A\widehat\otimes_k A,\qquad
\varepsilon:A\longrightarrow k,\qquad
S:A\longrightarrow A.
\]
Together with the multiplication and unit of \(A\), these maps make \(A\) a
**complete commutative Hopf algebra**: the ordinary tensor product in the
[[algebra-coalgebras/hopf-algebra|Hopf-algebra]] axioms is replaced by the
[[algebra-topological/completed-tensor-product|completed tensor product]].
The resulting topological Hopf algebra \(A=\mathcal O(G)\) is the **coordinate
Hopf algebra** of \(G\).

## The structure identities

The group axioms pull back, in the opposite direction, to
\[
(\Delta\widehat\otimes\operatorname{id})\Delta
=
(\operatorname{id}\widehat\otimes\Delta)\Delta,
\]
\[
(\varepsilon\widehat\otimes\operatorname{id})\Delta
=\operatorname{id}_A
=
(\operatorname{id}\widehat\otimes\varepsilon)\Delta,
\]
and
\[
m_A(S\widehat\otimes\operatorname{id})\Delta
=u_A\varepsilon
=m_A(\operatorname{id}\widehat\otimes S)\Delta.
\]
Thus \(\Delta\), \(\varepsilon\), and \(S\) encode multiplication, identity,
and inversion on \(G\), respectively. Although \(A\) is commutative as an
algebra, \(\Delta\) need not be cocommutative; cocommutativity of \(\Delta\)
is equivalent to commutativity of the [[formal-groups/formal-group|formal group]].

## Scope

This construction is affine. Non-affine formal groups require
sheaves of complete coordinate algebras rather than one global Hopf algebra.
Over more general bases, completed tensor products and formal spectra also
require explicit adic hypotheses. The precise
[[formal-groups/affine-formal-groups-and-complete-hopf-algebras|
anti-equivalence with complete Hopf algebras]] and the coordinate formula for
[[formal-groups/formal-group-laws-as-coordinates|formal group laws]] are
separate results. Finite-order duals at the augmentation form the
[[formal-groups/distribution-algebra|distribution algebra]].

## References

1. Michiel Hazewinkel, *Formal Groups and Applications*, Pure and Applied Mathematics 78, Academic Press, 1978; AMS reprint, 2012. [Publisher record](https://doi.org/10.1090/chel/078). Relevant: Chapters I and II on formal groups, formal group laws, and Hopf-algebra coordinates.
2. Michel Demazure and Pierre Gabriel, *Groupes algébriques, tome I: Géométrie algébrique, généralités, groupes commutatifs*, Masson, 1970. Relevant: the formal-group and formal-Lie-group constructions.
3. The Stacks Project Authors, *Formal Algebraic Spaces*, [Section 87.2: Formal schemes à la EGA](https://stacks.math.columbia.edu/tag/0AHY) and [Section 87.5: Completed tensor product](https://stacks.math.columbia.edu/tag/0AMU).
