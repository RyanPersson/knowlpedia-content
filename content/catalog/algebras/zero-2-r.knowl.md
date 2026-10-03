+++
id = "catalog/algebras/zero-2-r"
title = "Zero-product Jordan algebra R^2"
kind = "definition"
summary = "A 2-dimensional real Jordan algebra with identically zero product and no unit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["nonassociative-algebra/jordan-algebra", "linear-algebra/vector-space"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

The **zero-product Jordan algebra on \(\mathbb R^{2}\)** is the [[linear-algebra/vector-space|vector space]] \(\mathbb R^{2}\), with its usual addition and scalar multiplication, and with
\[
x\circ y=0\qquad\text{for all }x,y\in \mathbb R^{2}.
\]
This bilinear commutative product satisfies the [[nonassociative-algebra/jordan-algebra|Jordan identity]] because both sides are zero. Its dimension over \(\mathbb R\) is \(2\).

## No unit

The vector space has a nonzero vector \(x\), whereas \(e\circ x=0\) for every \(e\). Thus no element acts as a multiplicative unit. This is an object of [[catalog/categories/jordan-algebras|\(\mathbf{Jord}\)]] over the stated field, but is not an object of either [[catalog/categories/unital-jordan-algebras-arbitrary-maps|\(\mathbf{UJord}\)]] or [[catalog/categories/unital-jordan-algebras-unital-maps|\(\mathbf{Jord}_1\)]]. Positivity of the dimension matters: the zero-dimensional algebra is outside this family.

## Complete endomorphism and automorphism descriptions

Every \(\mathbb R\)-linear map \(T\) preserves the product, since
\[
T(x\circ y)=T(0)=0=T(x)\circ T(y).
\]
Conversely, a [[nonassociative-algebra/jordan-algebra-homomorphism|Jordan homomorphism]] over \(\mathbb R\) is required to be \(\mathbb R\)-linear. Therefore, in \(\mathbf{Jord}_{R}\),
\[
\operatorname{End}(\mathbb R^{2},0)=M_{2}(\mathbb R),
\qquad
\operatorname{Aut}(\mathbb R^{2},0)=\operatorname{GL}_{2}(\mathbb R).
\]
These identifications use the standard coordinate basis. On endomorphisms, composition becomes ordinary matrix multiplication and pointwise addition gives the matrix algebra. On automorphisms, composition gives the [[catalog/lie-groups/gl-2-r|general linear group \(\operatorname{GL}_{2}(\mathbb R)\)]]. Invertibility is sufficient because the inverse of an invertible [[linear-algebra/linear-map|linear map]] also preserves the zero product.

The resulting [[catalog/algebras/m-2-r|matrix algebra]] has its ordinary associative product, and is a different object from this zero-product Jordan algebra.
