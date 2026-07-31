+++
id = "probability/differential-entropy"
title = "Differential entropy"
kind = "definition"
summary = "The negative integral of a probability density times its logarithm, relative to Lebesgue measure."
aliases = ["differential-entropy", "Differential entropy"]
domains = ["probability"]
legacy_source_path = "probability/differential-entropy.md"
+++

Let \(X\) be an \(\mathbb R^d\)-valued [[probability/random-variable|random variable]] whose law has density \(f\) with respect to [[measure-theory/lebesgue-measure|Lebesgue measure]]. If the integral below is well-defined as an extended integral, the **differential entropy** of \(X\) is
\[
h(X)=-\int_{\mathbb R^d}f(x)\log f(x)\,dx,
\]
with \(0\log0:=0\).

The value may be \(+\infty\) or \(-\infty\). It is undefined if the positive and negative parts of \(f\log f\) both have infinite integral.

## Dependence on coordinates

Differential entropy is entropy relative to a chosen reference measure, here Lebesgue measure. It is therefore not invariant under changes of coordinates. If \(A\in\mathrm{GL}_d(\mathbb R)\), \(b\in\mathbb R^d\), and the entropies are defined, then
\[
h(AX+b)=h(X)+\log|\det A|.
\]
More generally, for a sufficiently regular diffeomorphism \(g\),
\[
h(g(X))
=
h(X)+\mathbb E\!\left[\log|\det Dg(X)|\right]
\]
whenever both sides are well-defined.

Unlike [[probability/shannon-entropy|Shannon entropy]], differential entropy can be negative. Coordinate-invariant comparisons are usually expressed through [[probability/relative-entropy-kl-divergence|relative entropy]].

## Examples

- If \(X\sim\mathcal N(\mu,\Sigma)\) on \(\mathbb R^d\) with positive-definite covariance \(\Sigma\), then
  \[
  h(X)=\frac12\log\!\bigl((2\pi e)^d\det\Sigma\bigr).
  \]
- If \(X\) is uniform on a measurable set \(A\subset\mathbb R^d\) with \(0<\lambda(A)<\infty\), then \(h(X)=\log\lambda(A)\).
