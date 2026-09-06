+++
id = "functional-analysis/weak-derivative"
title = "Weak derivative"
kind = "definition"
summary = "A weak derivative is a locally integrable function representing a function's distributional derivative."
aliases = ["Sobolev derivative", "generalized weak derivative"]
domains = ["functional-analysis", "partial-differential-equations", "sobolev-spaces"]
prerequisites = ["measure-theory/lebesgue-integrable-function", "functional-analysis/distributional-derivative", "measure-theory/almost-everywhere"]
dependency_heuristic = "semantic-full-review-v1"
dependency_review_count = 1
section_mode = "progressive"
+++

Let \(\Omega\subseteq\mathbb R^n\) be open and let \(f\) be locally
integrable, meaning [[measure-theory/lebesgue-integrable-function|Lebesgue
integrable]] on every compact subset of \(\Omega\). A locally integrable
function \(g\) is the **weak partial derivative** \(\partial_j f\) if
\[
\int_\Omega f\,\partial_j\varphi\,dx
=-\int_\Omega g\,\varphi\,dx
\]
for every \(\varphi\in C_c^\infty(\Omega)\). Equivalently, the
[[functional-analysis/distributional-derivative|distributional derivative]]
of the regular distribution defined by \(f\) is the regular distribution
defined by \(g\). A weak derivative, when it exists, is unique up to equality
[[measure-theory/almost-everywhere|almost everywhere]].

## Agreement with classical derivatives

If \(f\in C^1(\Omega)\), [[real-analysis/integration-by-parts|integration by parts]] shows that its classical
[[real-analysis/partial-derivative|partial derivative]] is also its weak derivative. More generally, a locally
[[analysis/absolute-continuity|absolutely continuous]] function on an interval
has a weak derivative equal almost everywhere to its ordinary derivative.
Weak differentiation therefore extends rather than replaces classical
differentiation.

## Existence and failure

The absolute-value function on \(\mathbb R\) has weak derivative
\(\operatorname{sgn}(x)\), even though it is not differentiable at \(0\).
The Heaviside function has no weak derivative represented by a locally
integrable function: its distributional derivative is \(\delta_0\).
Thus every locally integrable function has a distributional derivative, but
not every such derivative is weak in the function-valued sense.

## Sobolev-space role

A function belongs to the
[[functional-analysis/sobolev-space|Sobolev space]]
\(W^{1,p}(\Omega)\) when it and all its first weak derivatives belong to
\(L^p(\Omega)\); higher-order Sobolev spaces use weak derivatives indexed by
multi-indices. This makes differentiability compatible with norm completion
and variational methods.

## References

1. Lawrence C. Evans, *Partial Differential Equations*, 2nd ed., American Mathematical Society, 2010. [DOI record](https://doi.org/10.1090/gsm/019). Relevant: §5.2 on weak derivatives and Sobolev spaces.
2. Robert A. Adams and John J. F. Fournier, *Sobolev Spaces*, 2nd ed., Academic Press, 2003. [Publisher record](https://www.sciencedirect.com/book/9780120441433/sobolev-spaces). Relevant: Chapter 3 on weak derivatives.
