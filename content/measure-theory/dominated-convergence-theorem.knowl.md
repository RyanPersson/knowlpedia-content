+++
id = "measure-theory/dominated-convergence-theorem"
title = "Dominated convergence theorem"
kind = "knowl"
summary = "If measurable functions converge almost everywhere and are dominated by an integrable function, then integrals and L1 norms converge."
aliases = ["dominated-convergence-theorem", "Dominated convergence theorem"]
domains = ["measure-theory"]
legacy_source_path = "measure-theory/dominated-convergence-theorem.md"
+++

**Dominated convergence theorem.** Let $(X,\Sigma,\mu)$ be a [[measure-theory/measure-space|measure space]], and let $f_n,f:X\to\mathbb{R}$ (or $\mathbb{C}$) be [[measure-theory/measurable-function|measurable functions]] such that $f_n\to f$ [[measure-theory/almost-everywhere|almost everywhere]]. Suppose there is a nonnegative [[measure-theory/l1-function|$L^1$ function]] $g$ such that $|f_n|\le g$ almost everywhere for every $n$. Then $f$ is [[measure-theory/lebesgue-integrable-function|Lebesgue integrable]] and
$$
\lim_{n\to\infty}\int_X f_n\,d\mu \;=\; \int_X f\,d\mu,
\qquad\text{and}\qquad
\lim_{n\to\infty}\int_X |f_n-f|\,d\mu \;=\; 0.
$$
In particular, $f_n\to f$ in $L^1(\mu)$ (see [[measure-theory/convergence-in-lp|$L^p$ convergence]] with $p=1$).

Together with [[measure-theory/monotone-convergence-theorem|monotone convergence]] and [[measure-theory/fatous-lemma|Fatou's lemma]], this theorem is a core tool for interchanging limits with the [[measure-theory/lebesgue-integral|Lebesgue integral]]. It is especially useful when pointwise convergence is available but uniform bounds are only in the integrable sense.
