+++
id = "nonassociative-algebra/derivation-of-a-jordan-algebra"
title = "Derivation of a Jordan algebra"
kind = "definition"
summary = "A linear infinitesimal symmetry satisfying the Leibniz rule for the Jordan product."
aliases = ["Jordan derivation", "derivation algebra of a Jordan algebra", "Der(J)"]
domains = ["nonassociative-algebra", "lie-groups"]
prerequisites = ["nonassociative-algebra/jordan-algebra", "linear-algebra/linear-map", "linear-algebra/vector-space", "lie-groups/lie-algebra", "nonassociative-algebra/automorphism-group-of-a-jordan-algebra"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(J\) be a [[nonassociative-algebra/jordan-algebra|Jordan algebra]]. A
**derivation** of \(J\) is a [[linear-algebra/linear-map|linear map]] \(D:J\to J\) satisfying

\[
D(x\circ y)=D(x)\circ y+x\circ D(y)
\qquad(x,y\in J).
\]

The [[linear-algebra/vector-space|vector space]] of all derivations is denoted \(\operatorname{Der}(J)\).
With the commutator bracket
\([D,E]=D\circ E-E\circ D\), it is a
[[lie-groups/lie-algebra|Lie algebra]].

## Infinitesimal automorphisms

For a finite-dimensional real Jordan algebra, the
[[nonassociative-algebra/automorphism-group-of-a-jordan-algebra|automorphism
group]] is a [[fiber-bundles/lie-group|Lie group]] and

\[
\operatorname{Lie}(\operatorname{Aut}(J))=\operatorname{Der}(J).
\]

Indeed, differentiating a curve of product-preserving automorphisms gives the
Leibniz rule. Conversely, the exponential \(\exp(tD)\) of a derivation is a
one-parameter group of Jordan automorphisms. If \(J\) is unital, every
derivation fixes the unit infinitesimally: \(D(1)=0\).

## Inner derivations

Write \(L_x(y)=x\circ y\). In a Jordan algebra, each commutator

\[
[L_x,L_y]=L_xL_y-L_yL_x
\]

is a derivation. Derivations in the linear span of these commutators are
called **inner derivations**. This terminology is Jordan-theoretic: it should
not be confused with the associative-algebra formula \(a\mapsto xa-ax\),
since the Jordan product itself is commutative.

For finite-dimensional semisimple Jordan algebras over a field of
characteristic zero, every derivation is inner. In a [[nonassociative-algebra/euclidean-jordan-algebra|Euclidean Jordan algebra]],
derivations are skew-adjoint for the canonical
[[nonassociative-algebra/trace-form-of-a-euclidean-jordan-algebra|trace inner
product]], reflecting compactness of the automorphism group.

## References

1. Nathan Jacobson, *Structure and Representations of Jordan Algebras*,
   American Mathematical Society, 1968, Chapter VIII. [Publisher record](https://doi.org/10.1090/coll/039).
2. Richard D. Schafer, *An Introduction to Nonassociative Algebras*, Academic
   Press, 1966, Chapter IV. [Publisher record](https://shop.elsevier.com/books/an-introduction-to-nonassociative-algebras/schafer/978-0-12-374569-9).
