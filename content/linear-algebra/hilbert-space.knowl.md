+++
id = "linear-algebra/hilbert-space"
title = "Hilbert space"
kind = "knowl"
summary = "A complete inner product space."
aliases = ["hilbert-space", "Hilbert space"]
domains = ["linear-algebra"]
legacy_source_path = "linear-algebra/hilbert-space.md"
prerequisites = ["linear-algebra/inner-product-space", "linear-algebra/norm", "topology/complete-metric-space"]
dependency_heuristic = "semantic-spotcheck-review-v1"
dependency_review_count = 2
+++

A **Hilbert space** is an [[linear-algebra/inner-product-space|inner product space]] \((H,\langle\cdot,\cdot\rangle)\) that is complete with respect to the induced norm \(\|x\|=\sqrt{\langle x,x\rangle}\).

## Remarks

Here \(L^2(X,\mu)\) consists of equivalence classes of functions that agree
\(\mu\)-almost everywhere; this identification makes the positivity
condition definite.

With this induced norm, every Hilbert space is a [[linear-algebra/banach-space|Banach space]]. The [[linear-algebra/cauchy-schwarz-inequality|Cauchy–Schwarz inequality]] is a fundamental tool for relating inner products to norms in Hilbert space geometry.

## Examples

- \(\mathbb{R}^n\) with the usual dot product.
- For a [[measure-theory/measure-space|measure space]] \((X,\Sigma,\mu)\), the space \(L^2(X,\mu)\) of square-integrable functions with inner product \(\langle f,g\rangle=\int_X f\,\overline{g}\,d\mu\).
