+++
id = "catalog/algebras/spin-2-r"
title = "Spin factor J(R^2)"
kind = "definition"
summary = "Catalogue object: Spin factor J(R^2); scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["nonassociative-algebra/jordan-algebra", "linear-algebra/vector-space"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

The **spin-factor Jordan algebra \(J(\mathbb R^{2})\)** is \(\mathbb R\oplus\mathbb R^{2}\) with product
\[
(a,u)\circ(b,v)=(ab+\textstyle\sum_{i=1}^{2}u_iv_i,\;av+bu).
\]
The unit is \((1,0)\), and the dimension over \(\mathbb R\) is \(3\).

## Dimension parameter

The parameter \(2\) counts the vector summand, not the entire algebra. The full dimension is one larger. It is isomorphic to [[catalog/algebras/herm-2-r|\(\operatorname{Herm}_2(\mathbb R)\)]]. Writing a Hermitian matrix as \(\left(\begin{smallmatrix}a+t&z\\\overline z&a-t\end{smallmatrix}\right)\) gives the spin coordinates \((a,(t,z))\).

## Product check

Write \(B(u,v)=\sum_i u_iv_i\). Then \((a,u)^2=(a^2+B(u,u),2au)\). Substituting this expression into \(x^2\circ(x\circ y)=x\circ(x^2\circ y)\) gives equal scalar and vector components using only symmetry and bilinearity of \(B\); this verifies the Jordan identity. Unit-preserving and arbitrary [[nonassociative-algebra/jordan-algebra-homomorphism|Jordan homomorphisms]] therefore give separate catalogue categories on this object.

## References

1. [John C. Baez, The Octonions](https://math.ucr.edu/home/baez/octonions/node11.html), Section 3.3, spin-factor product and Hermitian two-by-two identification.
