+++
id = "measure-theory/essential-supremum"
title = "Essential supremum"
kind = "knowl"
summary = "Least upper bound of a measurable function after ignoring a null set."
aliases = ["essential-supremum", "Essential supremum"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/essential-supremum.md"
+++

The **essential supremum** of a [[measure-theory/measurable-function|measurable function]] $f:X\to\overline{\mathbb R}$ on a [[measure-theory/measure-space|measure space]] $(X,\Sigma,\mu)$ is the extended real number
$$
\operatorname*{ess\,sup}_{x\in X} f(x)
:= \inf\Bigl\{M\in\mathbb{R} : f(x)\le M \text{ for }\mu\text{-almost every }x\in X\Bigr\}.
$$

## Equivalent characterizations

Equivalently, $\operatorname*{ess\,sup}f$ is the [[real-analysis/infimum|infimum]] of the real numbers $M$ that bound $f$ above outside a [[measure-theory/null-set|null set]].

## Remarks

Unlike the pointwise [[real-analysis/supremum|supremum]], the essential supremum is unchanged if $f$ is modified on a null set. It therefore depends only on the [[measure-theory/ae-equality|almost-everywhere equivalence class]] of $f$, and it defines the $L^\infty$ norm through $\lVert f\rVert_\infty=\operatorname*{ess\,sup}|f|$.

## Examples

- On $([0,1],\mathcal B,\lambda)$, the function $f(x)=x$ has essential supremum $1$.
- On the same space, if $f(0)=1$ and $f(x)=0$ for $x>0$, then $\sup f=1$ but $\operatorname*{ess\,sup}f=0$.
