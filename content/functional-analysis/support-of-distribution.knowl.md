+++
id = "functional-analysis/support-of-distribution"
title = "Support of a distribution"
kind = "definition"
summary = "The support of a distribution is the complement of the largest open set on which the distribution vanishes."
aliases = ["distributional support"]
domains = ["functional-analysis", "distribution-theory"]
section_mode = "progressive"
+++

Let \(T\) be a [[functional-analysis/distribution|distribution]] on an open
set \(\Omega\subseteq\mathbb R^n\). The distribution **vanishes** on an open
subset \(U\subseteq\Omega\) if
\(\langle T,\varphi\rangle=0\) for every smooth [[functional-analysis/test-function-space|test function]] supported in
\(U\). The **support of \(T\)** is
\[
\operatorname{supp}T
=\Omega\setminus\bigcup\{U\subseteq\Omega:U\text{ is open and }T|_U=0\}.
\]
It is therefore a [[topology/closed-set|closed set]] relative to \(\Omega\),
and it is the smallest relatively closed set outside which \(T\) vanishes.
This definition depends only on the local action of \(T\) on test functions.

## Equivalent local criterion

A point \(x\in\Omega\) lies outside \(\operatorname{supp}T\) exactly when it
has an open neighborhood \(U\) such that \(T(\varphi)=0\) for every test
function \(\varphi\) supported in \(U\). Consequently, \(T=0\) if and only
if its support is empty. A partition-of-unity argument supplies the passage
from local vanishing to vanishing on arbitrary test functions supported in
the union.

## Functions, measures, and delta distributions

For a locally integrable function \(f\), the support of its regular
distribution is the complement of the largest open set on which \(f=0\)
[[measure-theory/almost-everywhere|almost everywhere]]; it can be smaller than the pointwise closure of
\(\{x:f(x)\ne0\}\) for a particular representative. The support of
\(\delta_a\) and of each derivative of \(\delta_a\) is the singleton
\(\{a\}\).

## Behavior under operations

Distributional differentiation cannot enlarge support:
\[
\operatorname{supp}(\partial^\alpha T)\subseteq\operatorname{supp}T.
\]
Multiplication by a smooth function \(a\) gives
\(\operatorname{supp}(aT)\subseteq\operatorname{supp}a\cap
\operatorname{supp}T\). [[functional-analysis/compactly-supported-distribution|Compactly supported distributions]] are precisely
those whose distributional support is
[[topology/compact-set|compact]]
[Hörmander, §2.3].

## References

1. Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, 2nd ed., Springer, 2003. [DOI record](https://doi.org/10.1007/978-3-642-61497-2). Relevant: §2.3 on support and singular support.
2. François Trèves, *Topological Vector Spaces, Distributions and Kernels*, Academic Press, 1967. [Publisher record](https://shop.elsevier.com/books/topological-vector-spaces-distributions-and-kernels/treves/978-1-4831-9859-0). Relevant: Chapter 24 on distributions and their support.
