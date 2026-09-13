+++
id = "shared-foundations/finite-product"
title = "Finite product"
kind = "definition"
summary = "An ordered finite multiplication, with the identity as the empty product."
aliases = ["empty product"]
domains = ["shared-foundations"]
section_mode = "progressive"
prerequisites = ["shared-foundations/natural-numbers", "shared-foundations/function", "algebra-groups/monoid"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 1
+++

For elements \(a_1,\ldots,a_n\) of a [[algebra-groups/monoid|monoid]] with identity \(1\), their **finite product** is defined recursively by
\[
\prod_{j=1}^{0}a_j=1,\qquad
\prod_{j=1}^{n+1}a_j=\left(\prod_{j=1}^{n}a_j\right)a_{n+1}.
\]
Associativity permits changing parentheses. Reordering requires commutativity or a separate argument that the relevant elements commute. The empty-product convention is an identity for multiplication, not a statement that zero factors give the number zero.

## Examples

Products of real or complex numbers can be reordered. Products of square matrices generally cannot: \(AB\) need not equal \(BA\). The factorial \(n!\) is a product of the integers from one to \(n\), so \(0!=1\).
