+++
id = "catalog/algebras/zero-n-c"
title = "Zero-product Jordan algebra C^n"
kind = "definition"
summary = "A n-dimensional complex Jordan algebra with identically zero product and no unit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["nonassociative-algebra/jordan-algebra", "linear-algebra/vector-space"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

For every positive integer \(n\), The **zero-product Jordan algebra on \(\mathbb C^{n}\)** is the [[linear-algebra/vector-space|vector space]] \(\mathbb C^{n}\), with its usual addition and scalar multiplication, and with
\[
x\circ y=0\qquad\text{for all }x,y\in \mathbb C^{n}.
\]
This bilinear commutative product satisfies the [[nonassociative-algebra/jordan-algebra|Jordan identity]] because both sides are zero. Its dimension over \(\mathbb C\) is \(n\).

## No unit

The vector space has a nonzero vector \(x\), whereas \(e\circ x=0\) for every \(e\). Thus no element acts as a multiplicative unit. This is an object of [[catalog/categories/jordan-algebras|\(\mathbf{Jord}\)]] over the stated field, but is not an object of either [[catalog/categories/unital-jordan-algebras-arbitrary-maps|\(\mathbf{UJord}\)]] or [[catalog/categories/unital-jordan-algebras-unital-maps|\(\mathbf{Jord}_1\)]]. Positivity of the dimension matters: the zero-dimensional algebra is outside this family.

## Complete endomorphism and automorphism descriptions

Every \(\mathbb C\)-linear map \(T\) preserves the product, since
\[
T(x\circ y)=T(0)=0=T(x)\circ T(y).
\]
Conversely, a [[nonassociative-algebra/jordan-algebra-homomorphism|Jordan homomorphism]] over \(\mathbb C\) is required to be \(\mathbb C\)-linear. Therefore, in \(\mathbf{Jord}_{C}\),
\[
\operatorname{End}(\mathbb C^{n},0)=M_{n}(\mathbb C),
\qquad
\operatorname{Aut}(\mathbb C^{n},0)=\operatorname{GL}_{n}(\mathbb C).
\]
These identifications use the standard coordinate basis. On endomorphisms, composition becomes ordinary matrix multiplication and pointwise addition gives the matrix algebra. On automorphisms, composition gives the [[catalog/lie-groups/gl-n-c|general linear group \(\operatorname{GL}_{n}(\mathbb C)\)]]. Invertibility is sufficient because the inverse of an invertible [[linear-algebra/linear-map|linear map]] also preserves the zero product.

The resulting [[catalog/algebras/m-n-c|matrix algebra]] has its ordinary associative product, and is a different object from this zero-product Jordan algebra.

## Restricting the scalar field

As a real Jordan algebra this object has dimension \(2n\), still with zero product. The same proof gives real-linear endomorphism algebra \(M_{2n}(\mathbb R)\) and [[nonassociative-algebra/automorphism-group-of-a-jordan-algebra|automorphism group]] \(\operatorname{GL}_{2n}(\mathbb R)\), after choosing the real basis obtained from the complex coordinate basis and its multiples by \(i\). These are larger collections of maps than the complex-linear ones. For example, coordinatewise complex conjugation is a real-linear automorphism but is not complex-linear.
