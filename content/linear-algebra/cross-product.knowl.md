+++
id = "linear-algebra/cross-product"
title = "Cross product in three-dimensional Euclidean space"
kind = "definition"
summary = "The oriented bilinear product of two real three-vectors."
aliases = ["cross product", "vector product"]
domains = ["linear-algebra"]
section_mode = "progressive"
prerequisites = ["linear-algebra/euclidean-space", "linear-algebra/determinant"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

In the standard oriented coordinates of [[linear-algebra/euclidean-space|Euclidean space]] \(\mathbb R^3\), the **cross product** is
\[
a\times b=(a_2b_3-a_3b_2,\ a_3b_1-a_1b_3,\ a_1b_2-a_2b_1).
\]
It is bilinear, satisfies \(a\times b=-b\times a\), and obeys
\((a\times b)\cdot c=\det[a\ b\ c]\). Thus it is perpendicular to both inputs. Reversing the orientation reverses the sign of the product.

## Vector identity

Direct expansion gives \(a\times(b\times c)=b(a\cdot c)-c(a\cdot b)\). In particular, \(a\times(a\times b)=-|a|^2b\) when \(a\cdot b=0\). This identity recovers a transverse vector from a curl symbol in Fourier calculations.
