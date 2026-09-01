+++
id = "nonassociative-algebra/jordan-idempotent"
title = "Jordan idempotent"
kind = "definition"
summary = "An element e of a Jordan algebra satisfying e composed with e equals e."
aliases = ["idempotent in a Jordan algebra", "Jordan algebra idempotent"]
domains = ["nonassociative-algebra"]
prerequisites = ["nonassociative-algebra/jordan-algebra", "nonassociative-algebra/special-and-exceptional-jordan-algebras"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

An element \(e\) of a [[nonassociative-algebra/jordan-algebra|Jordan
algebra]] \(J\) is a **Jordan idempotent** when
\[
e\circ e=e.
\]
In a [[nonassociative-algebra/special-and-exceptional-jordan-algebras|special Jordan algebra]] whose product is
\(x\circ y=(xy+yx)/2\), this is exactly the usual equation \(e^2=e\).

## Role in the structure theory

Left Jordan multiplication by \(e\),
\(L_e(x)=e\circ x\), organizes \(J\) into its
[[nonassociative-algebra/peirce-decomposition|Peirce spaces]]. In a unital
[[nonassociative-algebra/euclidean-jordan-algebra|Euclidean Jordan algebra]], idempotents behave like [[linear-algebra/orthogonal-projection|orthogonal projections]]:
they can be decomposed into
[[nonassociative-algebra/primitive-jordan-idempotent|primitive idempotents]],
and maximal compatible decompositions form [[nonassociative-algebra/jordan-frame|Jordan frames]].

The comparison with projections is exact for
[[nonassociative-algebra/hermitian-matrix-jordan-algebra|Hermitian-matrix
Jordan algebras]]. There an element is a Jordan idempotent precisely when it
is a self-adjoint projection, and its Jordan rank agrees with the ordinary
matrix rank.

## References

1. Kevin McCrimmon, *A Taste of Jordan Algebras*, Springer, 2004, §§5.1 and 13.1. [Publisher record](https://doi.org/10.1007/b97489).
2. Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones*, Oxford University Press, 1994, Chapter III. [Publisher record](https://doi.org/10.1093/oso/9780198534778.001.0001).
