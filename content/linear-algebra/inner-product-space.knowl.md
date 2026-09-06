+++
id = "linear-algebra/inner-product-space"
title = "Inner product space"
kind = "knowl"
summary = "A vector space equipped with an inner product."
aliases = ["inner-product-space", "Inner product space"]
domains = ["linear-algebra"]
prerequisites = ["linear-algebra/vector-space", "linear-algebra/inner-product"]
dependency_review_count = 1
legacy_source_path = "linear-algebra/inner-product-space.md"
+++

An **inner product space** is a [[linear-algebra/vector-space|vector space]] \(V\) over \(\mathbb{R}\) or \(\mathbb{C}\) together with a specified [[linear-algebra/inner-product|inner product]] \(\langle\cdot,\cdot\rangle\) on \(V\).

## Remarks

Every inner product space is automatically a [[linear-algebra/normed-vector-space|normed vector space]] via \(\|v\|=\sqrt{\langle v,v\rangle}\), and many constructions in linear algebra are organized by [[linear-algebra/orthogonality|orthogonality]]. A complete inner product space is a [[linear-algebra/hilbert-space|Hilbert space]].

## Examples

- \(\mathbb{R}^n\) with the standard dot product is an inner product space.
- \(\mathbb{C}^n\) with the standard Hermitian product is an inner product space.
- The real vector space of real polynomials on \([0,1]\) with \(\langle p,q\rangle=\int_0^1 p(t)q(t)\,dt\) is an inner product space.

Over \(\mathbb C\), use \(\langle p,q\rangle=\int_0^1 p(t)\overline{q(t)}\,dt\).
The polynomial space is not complete for this integral norm, so an inner
product space need not be a Hilbert space.
