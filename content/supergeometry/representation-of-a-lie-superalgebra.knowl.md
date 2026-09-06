+++
id = "supergeometry/representation-of-a-lie-superalgebra"
title = "Representation of a Lie superalgebra"
kind = "definition"
summary = "An even Lie-superalgebra morphism from a Lie superalgebra to the super-endomorphisms of a super vector space."
aliases = ["Lie superalgebra representation", "superrepresentation of a Lie superalgebra"]
domains = ["supergeometry", "representation-theory"]
prerequisites = ["supergeometry/lie-superalgebra", "supergeometry/super-vector-space", "supergeometry/super-internal-hom", "supergeometry/supercommutator", "linear-algebra/vector-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\mathfrak g\) be a [[supergeometry/lie-superalgebra|Lie
superalgebra]] and let \(V\) be a
[[supergeometry/super-vector-space|super vector space]]. A
**representation of \(\mathfrak g\) on \(V\)** is an even Lie-superalgebra
morphism
\[
\rho:\mathfrak g\longrightarrow\mathfrak{gl}(V),
\]
where
\(\mathfrak{gl}(V)=\underline{\operatorname{End}}(V)\) is the
[[supergeometry/super-internal-hom|super internal endomorphism space]] with
its [[supergeometry/supercommutator|supercommutator]] bracket.

Equivalently, homogeneous \(x\in\mathfrak g\) acts by an endomorphism of
parity \(|x|\), and
\[
\rho([x,y])
=\rho(x)\rho(y)-(-1)^{|x||y|}\rho(y)\rho(x).
\]
The **adjoint representation** is the action on \(\mathfrak g\) given by
\(\operatorname{ad}_x(y)=[x,y]\). The super Jacobi identity is exactly the
identity that makes this a representation.

## References

1. M. Scheunert, *The Theory of Lie Superalgebras*, Lecture Notes in
   Mathematics 716, Springer, 1979. [Publisher
   record](https://doi.org/10.1007/BFb0073442). Relevant: Chapter 1.
2. I. M. Musson, *Lie Superalgebras and Enveloping Algebras*, American
   Mathematical Society, 2012. [Publisher
   record](https://doi.org/10.1090/gsm/131). Relevant: Chapters 1–2.
