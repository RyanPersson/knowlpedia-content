+++
id = "nonassociative-algebra/jordan-algebra"
title = "Jordan algebra"
kind = "definition"
summary = "A commutative algebra satisfying the Jordan identity."
aliases = ["Jordan algebra", "Jordan-algebra"]
domains = ["nonassociative-algebra"]
prerequisites = ["linear-algebra/vector-space"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(k\) be a field of characteristic different from \(2\). A **Jordan
algebra over \(k\)** is a [[linear-algebra/vector-space|vector space]] \(J\)
with a bilinear product \(x\circ y\) satisfying
\[
x\circ y=y\circ x,
\qquad
x^2\circ(x\circ y)=x\circ(x^2\circ y),
\qquad x^2:=x\circ x.
\]
The second equation is the **Jordan identity**. A Jordan algebra need not be
associative or unital unless those conditions are stated separately.

## Why this identity

The Jordan identity implies [[nonassociative-algebra/power-associative-algebra|power associativity]]: every expression involving
only one element \(x\) has an unambiguous value. Thus \(x^n\), polynomials in
\(x\), and spectral notions can be defined even though arbitrary products of
three elements may depend on their parentheses.

The motivating construction starts with an associative \(k\)-algebra \(A\).
Its symmetrized product
\[
x\circ y=\frac12(xy+yx)
\]
turns the underlying vector space into a Jordan algebra, denoted \(A^+\).
The product is generally nonassociative even when \(A\) is associative.

## Units and operators

A unit is an element \(e\) satisfying \(e\circ x=x\) for every \(x\in J\).
When it exists it is unique. The multiplication operator associated to \(x\)
is \(L_x(y)=x\circ y\). The Jordan identity can be written
\([L_x,L_{x^2}]=0\).

The unit convention matters for [[nonassociative-algebra/jordan-subalgebra|Jordan
subalgebras]] and [[nonassociative-algebra/jordan-algebra-homomorphism|Jordan
homomorphisms]]: product preservation alone does not force an inclusion or a
non-surjective map to preserve units.

## Important classes

Jordan algebras that embed in some \(A^+\) are
[[nonassociative-algebra/special-and-exceptional-jordan-algebras|special]];
those that do not are exceptional. Finite-dimensional real Jordan algebras
with a compatible positive-definite [[linear-algebra/inner-product|inner product]] are
[[nonassociative-algebra/euclidean-jordan-algebra|Euclidean Jordan algebras]].

## Characteristic caveat

The displayed definition is standard in characteristic different from \(2\).
In characteristics \(2\) and \(3\), linearized identities can lose information,
and the most robust general theory uses quadratic Jordan algebras. Those
variants should not be silently substituted for the convention used here.

## References

1. Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones*, Oxford University Press, 1994. [Publisher record](https://global.oup.com/academic/product/analysis-on-symmetric-cones-9780198534778).
2. Pascual Jordan, John von Neumann, and Eugene Wigner, “On an Algebraic Generalization of the Quantum Mechanical Formalism,” *Annals of Mathematics* 35 (1934), 29–64. [JSTOR record](https://www.jstor.org/stable/1968117).
3. Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups*, Springer, 2000. [Publisher record](https://link.springer.com/book/10.1007/978-3-662-12622-6).
