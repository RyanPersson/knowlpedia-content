+++
id = "measure-theory/product-measure"
title = "Product measure"
kind = "knowl"
summary = "A measure on a product space determined by its values on measurable rectangles."
aliases = ["product-measure", "Product measure"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/product-measure.md"
prerequisites = ["shared-foundations/cartesian-product", "measure-theory/measure-space", "measure-theory/sigma-algebra", "measure-theory/measurable-rectangle", "measure-theory/sigma-finite-measure", "measure-theory/product-sigma-algebra"]
dependency_heuristic = "navier-semantic-review-v1"
dependency_review_count = 3
+++

A **product measure** combines two measures into a measure on a [[shared-foundations/cartesian-product|Cartesian product]]. Let \((X,\mathcal{A},\mu)\) and \((Y,\mathcal{B},\nu)\) be [[measure-theory/measure-space|measure spaces]]. Their [[measure-theory/product-sigma-algebra|product sigma-algebra]] is denoted by \(\mathcal A\otimes\mathcal B\). A measure \(\mu\otimes\nu\) on \((X\times Y,\mathcal{A}\otimes\mathcal{B})\) is called a **product measure** if
\[
(\mu\otimes\nu)(A\times B)=\mu(A)\,\nu(B)
\quad\text{for all }A\in\mathcal{A},\ B\in\mathcal{B}.
\]

When \(\mu\) and \(\nu\) are \(\sigma\)-finite, such a measure exists and is uniquely determined by its values on rectangles; it is the measure used in [[measure-theory/tonellis-theorem|Tonelli's theorem]] and [[measure-theory/fubinis-theorem|Fubini's theorem]] for iterated integration.

## Examples

- If \(\lambda\) is [[measure-theory/lebesgue-measure|Lebesgue measure]] on \(\mathbb{R}\), the [[measure-theory/measure-completion|completion]] of \(\lambda\otimes\lambda\) is Lebesgue measure on \(\mathbb{R}^2\); the product sigma-algebra itself need not be complete. The analogous completion gives Lebesgue measure in higher dimensions.
- If \(\mu\) and \(\nu\) are counting measures on \(\mathbb{N}\), then \(\mu\otimes\nu\) is counting measure on \(\mathbb{N}\times\mathbb{N}\): for any finite set \(E\subset \mathbb{N}\times\mathbb{N}\) one has \((\mu\otimes\nu)(E)=|E|\).
