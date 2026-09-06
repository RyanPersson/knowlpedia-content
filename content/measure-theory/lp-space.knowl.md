+++
id = "measure-theory/lp-space"
title = "L^p space"
kind = "knowl"
summary = "Measurable functions with finite L^p norm, identified up to equality almost everywhere."
aliases = ["lp-space", "L^p space"]
domains = ["measure-theory"]
prerequisites = ["measure-theory/measure-space","measure-theory/lp-norm","measure-theory/almost-everywhere"]
dependency_review_count = 1
legacy_source_path = "measure-theory/lp-space.md"
+++

For a [[measure-theory/measure-space|measure space]] \((X,\Sigma,\mu)\) and \(1\le p\le\infty\), the **\(L^p\) space** is
\[
L^p(X,\Sigma,\mu)
:=\{f:X\to\mathbb F\text{ measurable}:\|f\|_p<\infty\}/\mathord{\sim},
\]
where \(\mathbb F\) is \(\mathbb R\) or \(\mathbb C\), \(\|f\|_p\) is the [[measure-theory/lp-norm|\(L^p\) norm]], and \(f\sim g\) means that \(f=g\) [[measure-theory/almost-everywhere|almost everywhere]].

The quotient makes the \(L^p\) norm a genuine norm rather than a seminorm. The cases \(p=1\) and \(p=\infty\) correspond to [[measure-theory/l1-function|\(L^1\) functions]] and [[measure-theory/l-infinity-function|\(L^\infty\) functions]], respectively.

## Examples

- On \(((0,1),\mathcal B,\lambda)\), the function \(f(x)=x^{-1/2}\) lies in \(L^1\) but not in \(L^2\).
- On \((\mathbb R,\mathcal B,\lambda)\), the indicator \(\mathbf 1_{[0,1]}\) lies in \(L^p\) for every \(1\le p\le\infty\), and its \(L^p\) norm is \(1\).
