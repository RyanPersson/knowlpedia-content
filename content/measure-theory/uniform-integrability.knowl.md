+++
id = "measure-theory/uniform-integrability"
title = "Uniform integrability"
kind = "knowl"
summary = "A uniform L1 bound together with uniformly vanishing large-value tails."
aliases = ["uniform-integrability", "Uniform integrability"]
domains = ["measure-theory"]
prerequisites = ["measure-theory/measure-space","shared-foundations/sequence"]
dependency_review_count = 1
legacy_source_path = "measure-theory/uniform-integrability.md"
+++

A family \(\mathcal F\subset L^1(X,\mu)\) on a [[measure-theory/measure-space|measure space]] \((X,\mathcal A,\mu)\) is **uniformly integrable** if
\[
\sup_{f\in\mathcal F}\|f\|_1<\infty
\qquad\text{and}\qquad
\lim_{M\to\infty}\ \sup_{f\in\mathcal{F}} \int_{\{|f|>M\}} |f|\,d\mu = 0.
\]

When \(\mu(X)<\infty\), the tail condition alone implies the uniform \(L^1\) bound.

A [[shared-foundations/sequence|sequence]] \((f_n)\) is uniformly integrable if the family \(\{f_n:n\ge 1\}\) is uniformly integrable.

## Interpretation

The condition rules out increasingly tall tails that retain substantial \(L^1\)-mass. Together with suitable convergence hypotheses, it permits passage to limits in the [[measure-theory/lebesgue-integral|Lebesgue integral]].

## Examples

- If \(|f|\le g\) almost everywhere for every \(f\in\mathcal F\), where \(g\in L^1(X,\mu)\), then \(\mathcal F\) is uniformly integrable.
- On \(([0,1],\mathcal B,\lambda)\), the functions \(f_n=n\mathbf 1_{[0,1/n]}\) are not uniformly integrable: for any \(M>0\), choose \(n>M\). Then
  \[
  \int_{\{|f_n|>M\}} |f_n|\,d\lambda = \int_0^{1/n} n\,dx = 1,
  \]
  so the supremum of the tail integrals does not tend to \(0\).
