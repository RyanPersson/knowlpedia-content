+++
id = "real-analysis/differentiation-rules"
title = "Differentiation rules"
kind = "knowl"
summary = "Formulas for derivatives of sums, products, quotients, and compositions."
aliases = ["differentiation-rules", "Differentiation rules"]
domains = ["real-analysis"]
prerequisites = ["real-analysis/interval", "real-analysis/differentiability-1d"]
dependency_review_count = 1
legacy_source_path = "real-analysis/differentiation-rules.md"
+++

Let \(I\subseteq\mathbb R\) be an [[real-analysis/interval|interval]], let \(g:I\to J\) and \(f:J\to\mathbb R\) be functions on intervals, and fix an interior point \(x\in I\). Assume \(f\) and \(g\) are [[real-analysis/differentiability-1d|differentiable]] at the points where they are used. Then:

- **Linearity.** For \(c\in\mathbb R\),
  \[
  (f+g)'(x)=f'(x)+g'(x),\qquad (cf)'(x)=c\,f'(x).
  \]
- **Product rule.**
  \[
  (fg)'(x)=f'(x)g(x)+f(x)g'(x).
  \]

- **Quotient rule.** If \(g(x)\neq 0\), then
  \[
  \left(\frac{f}{g}\right)'(x)=\frac{f'(x)g(x)-f(x)g'(x)}{(g(x))^2}.
  \]

- **Chain rule.** If \(g\) is differentiable at \(x\) and \(f\) is differentiable at \(g(x)\), then
  \[
  (f\circ g)'(x)=f'(g(x))\,g'(x).
  \]

## Remarks

The multivariable [[real-analysis/chain-rule|chain rule]] extends the last identity to differentiable maps between Euclidean spaces.
