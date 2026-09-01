+++
id = "nonassociative-algebra/special-and-exceptional-jordan-algebras"
title = "Special and exceptional Jordan algebras"
kind = "definition"
summary = "The distinction between Jordan algebras realizable by symmetrizing associative multiplication and those that are not."
aliases = ["special Jordan algebra", "special versus exceptional Jordan algebra"]
domains = ["nonassociative-algebra"]
prerequisites = ["nonassociative-algebra/jordan-algebra", "nonassociative-algebra/jordan-subalgebra"]
dependency_heuristic = "definition-links-v1"
dependency_review_count = 0
section_mode = "progressive"
+++

A [[nonassociative-algebra/jordan-algebra|Jordan algebra]] \(J\) is **special**
if it is isomorphic to a [[nonassociative-algebra/jordan-subalgebra|Jordan subalgebra]] of \(A^+\) for some associative
algebra \(A\), where
\[
x\circ y=\frac12(xy+yx).
\]
A Jordan algebra that is not special is **exceptional**.

## What the definition does and does not say

“Special” means embeddable into a symmetrized associative algebra; it does not
mean that the Jordan product itself is associative. Likewise, “exceptional”
is a property, not the name of a unique algebra. Nevertheless, the phrase
**the exceptional Jordan algebra** conventionally denotes the 27-dimensional
real [[nonassociative-algebra/exceptional-jordan-algebra|Albert algebra]] \(\mathfrak h_3(\mathbb O)\).

The embedding in the definition need not preserve units unless a unital
embedding is explicitly required. This distinction is useful when Jordan
algebras occur as matrix corners.

## Fundamental examples

The self-adjoint part of an associative real or complex matrix algebra is
special. This includes \(\mathfrak h_n(\mathbb R)\),
\(\mathfrak h_n(\mathbb C)\), and \(\mathfrak h_n(\mathbb H)\) with their
symmetrized matrix product.

The real algebra \(\mathfrak h_3(\mathbb O)\) is exceptional: it satisfies the
Jordan identity but admits no embedding into \(A^+\) for any associative
algebra \(A\). Its existence is the exceptional case in the classification of
finite-dimensional [[nonassociative-algebra/simple-euclidean-jordan-algebra|simple Euclidean Jordan algebras]].

## Identities

Every special Jordan algebra satisfies all polynomial identities inherited
from symmetrized associative multiplication. Exceptional Jordan algebras are
detected by identities that hold in all special Jordan algebras but fail in
the exceptional case; the first classical example is the Glennie identity.

## References

1. Pascual Jordan, John von Neumann, and Eugene Wigner, “On an Algebraic Generalization of the Quantum Mechanical Formalism,” *Annals of Mathematics* 35 (1934), 29–64. [JSTOR record](https://www.jstor.org/stable/1968117).
2. Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups*, Springer, 2000. [Publisher record](https://link.springer.com/book/10.1007/978-3-662-12622-6).
