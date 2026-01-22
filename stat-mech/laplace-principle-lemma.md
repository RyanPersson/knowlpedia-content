---
title: "Laplace Principle"
description: "Asymptotic evaluation of log-integrals of exp(n f) by the supremum of f; a deterministic precursor to Varadhan’s lemma."
---

This lemma is a deterministic prototype for {{< knowl id="varadhans-lemma" section="large-deviations" text="Varadhan's lemma" >}} and is closely related to the {{< knowl id="large-deviation-principle" section="large-deviations" text="large deviation principle" >}}. It is frequently used to approximate partition functions and free energies via maximization.

## Statement
Let $K$ be a compact topological space and let $\mu$ be a finite Borel measure on $K$ such that every nonempty open set has positive $\mu$-measure. If $f:K\to\mathbb{R}$ is continuous, then
$$
\lim_{n\to\infty}\frac{1}{n}\log\!\int_K e^{n f(x)}\,\mu(dx)
={}
\max_{x\in K} f(x).
$$

More generally, if $f$ is upper semicontinuous and bounded above on compact $K$, the same conclusion holds with $\max$ replaced by $\sup$.

## Key hypotheses and conclusions
**Hypotheses**
- Compactness of $K$ (ensures $f$ attains its maximum when $f$ is continuous).
- $\mu$ does not ignore neighborhoods of maximizers (positivity on open sets).
- Regularity of $f$ (at least continuity for the simplest version).

**Conclusions**
- Exponential integrals are governed at leading order by the **global maximum** of $f$:
  the integral behaves like $\exp\big(n\max f\big)$ up to subexponential factors.
- A discrete analogue: for finitely many numbers $\{a_i\}$,
  $\lim_{n\to\infty}\frac1n\log\sum_i e^{n a_i}=\max_i a_i$.

## Proof idea / significance
Let $M=\max_K f$. For the upper bound, $\int_K e^{n f}\,d\mu\le e^{nM}\mu(K)$ gives
$\limsup \le M$. For the lower bound, choose $x_\star\in K$ with $f(x_\star)=M$ and a neighborhood $U$ where $f\ge M-\varepsilon$. Then
$\int_K e^{n f}\,d\mu\ge \int_U e^{n f}\,d\mu\ge \mu(U)\,e^{n(M-\varepsilon)}$,
so $\liminf \ge M-\varepsilon$ and let $\varepsilon\downarrow 0$.

In statistical mechanics, this principle explains why a partition function (an integral or sum of exponentials) yields a free energy that can often be expressed as a variational supremum. It is the leading-order version of the more refined {{< knowl id="saddle-point-lemma" text="saddle-point method" >}}, which also provides prefactors.
