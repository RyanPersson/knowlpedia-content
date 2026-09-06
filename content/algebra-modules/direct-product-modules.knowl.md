+++
id = "algebra-modules/direct-product-modules"
title = "Direct product of modules"
kind = "knowl"
summary = "The product of modules: all tuples with coordinatewise operations."
aliases = ["direct-product-modules", "Direct product of modules"]
domains = ["algebra-modules"]
legacy_source_path = "algebra-modules/direct-product-modules.md"
prerequisites = ["algebra-modules/module", "shared-foundations/cartesian-product"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
+++

Given a family of \(R\)-[[algebra-modules/module|modules]] \((M_i)_{i\in I}\), their **direct product** is
\[
\prod_{i\in I} M_i=\{(m_i)_{i\in I}: m_i\in M_i\},
\]
with coordinatewise addition and scalar multiplication. As a set it is the [[shared-foundations/cartesian-product|Cartesian product]], and it satisfies the categorical product universal property: for every \(R\)-module \(X\), giving a homomorphism \(X\to \prod_i M_i\) is equivalent to giving a homomorphism \(X\to M_i\) for each \(i\).

## Remarks

For infinite \(I\), the product contains the [[algebra-modules/direct-sum-modules|direct sum]] and may also contain tuples with infinitely many nonzero coordinates. For example, \(\bigoplus_{n\ge1}\mathbb Z\) is strictly contained in \(\prod_{n\ge1}\mathbb Z\).

## Examples

- \(\prod_{n\ge 1}\mathbb Z\) is the set of all integer sequences, with no finiteness restriction.
- For modules \(M,N\), the product \(M\times N\) is the usual binary product with projections.
- If each \(M_i=0\), then the product is \(0\), even if \(I\) is infinite.
