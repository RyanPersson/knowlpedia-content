+++
id = "catalog/algebras/m-1-c-jordan"
title = "Full-matrix Jordan algebra M_1(C)^+"
kind = "definition"
summary = "Catalogue object: Full-matrix Jordan algebra M_1(C)^+; scalar field, operations, and dimension are explicit."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["catalog/algebras/m-1-c", "nonassociative-algebra/jordan-algebra"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

The **full-matrix Jordan algebra \(M_{1}(\mathbb C)^+\)** has the same [[linear-algebra/vector-space|vector space]] as [[catalog/algebras/m-1-c|\(M_{1}(\mathbb C)\)]], but the product is
\[
X\circ Y=\tfrac12(XY+YX).
\]
The unit is \(I_{1}\). This object includes all square matrices; self-adjointness is not required.

## Why it is Jordan

The new product is commutative. Expanding both sides of \(X^2\circ(X\circ Y)=X\circ(X^2\circ Y)\) in the original associative product gives the same four terms, which proves the Jordan identity. The matrix-entry coordinates still give dimension \(1^2\) over \(\mathbb C\).

## Category distinction

The associative matrix object and this Jordan object retain separate records because their multiplications differ. The symmetrization is a construction, not an assertion that the identity map is a multiplicative homomorphism between the two products. A Jordan map need preserve only the symmetrized product. At size one both products coincide.
