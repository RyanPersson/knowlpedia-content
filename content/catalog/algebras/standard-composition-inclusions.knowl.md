+++
id = "catalog/algebras/standard-composition-inclusions"
title = "Standard inclusions in the Cayley–Dickson tower"
kind = "theorem"
summary = "Standard inclusions in the Cayley–Dickson tower."
aliases = []
domains = ["catalog", "nonassociative-algebra"]
section_mode = "progressive"
prerequisites = ["catalog/algebras/sedenions"]
dependency_heuristic = "catalog-semantic-prerequisites-v1"
dependency_review_count = 0
+++

The **standard Cayley–Dickson tower** gives injective unital real-algebra maps
\[
\mathbb R\hookrightarrow\mathbb C\hookrightarrow\mathbb H
\hookrightarrow\mathbb O\hookrightarrow\mathbb S.
\]
At each doubling, the inclusion is \(a\mapsto(a,0)\). Here the last object is the [[catalog/algebras/sedenions|real sedenion algebra]]; all arrows are interpreted in the category of real algebras with no associativity requirement.

## Verification

In a Cayley–Dickson product, \((a,0)(b,0)=(ab,0)\). This proves product preservation; linearity, preservation of one, and injectivity follow from the coordinates. Standard conjugation also restricts correctly. The inclusion of \(\mathbb C\) in \(\mathbb H\) uses the chosen quaternion generator \(i\).

## Category boundary

The first three objects are associative; the octonions and sedenions are not. The final arrow cannot be an arrow in the category of [[nonassociative-algebra/composition-algebra|composition algebras]], since sedenions do not have a multiplicative nondegenerate quadratic norm. Likewise, choosing the complex subalgebra inside \(\mathbb H\) does not make quaternion multiplication complex-bilinear.
