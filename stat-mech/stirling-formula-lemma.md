---
title: "Stirling's Formula"
description: "Asymptotic approximation for n! and log n!, used for entropy and large-N counting in statistical mechanics."
---

Stirling’s formula is a basic asymptotic tool for combinatorial and phase-space counting, and it is frequently used when connecting microscopic counting to {{< knowl id="boltzmann-entropy-microcanonical" section="stat-mech" text="Boltzmann entropy" >}} and to information-theoretic quantities like {{< knowl id="shannon-entropy" section="probability" text="Shannon entropy" >}}.

## Statement
As $n\to\infty$,
$$
n! \sim \sqrt{2\pi n}\,\Big(\frac{n}{e}\Big)^n.
$$
Equivalently,
$$
\log(n!) = n\log n - n + \tfrac12\log(2\pi n) + o(1).
$$

A common quantitative refinement is: for every integer $n\ge 1$ there exists $\theta_n\in(0,1)$ such that
$$
n! = \sqrt{2\pi n}\,\Big(\frac{n}{e}\Big)^n \exp\!\Big(\frac{\theta_n}{12n}\Big).
$$
In particular,
$$
\log(n!) = n\log n - n + \tfrac12\log(2\pi n) + O\!\Big(\frac{1}{n}\Big).
$$

## Key hypotheses and conclusions
**Hypotheses**
- $n\in\mathbb{N}$ and $n\to\infty$.

**Conclusions**
- Accurate leading-order and next-order asymptotics for $n!$ and $\log(n!)$.
- Enables asymptotics for multinomial coefficients; e.g. leading terms produce entropy-like functionals.

## Proof idea / significance
One proof route uses integral bounds for $\log(n!)=\sum_{k=1}^n \log k$ compared to $\int_1^n \log x\,dx$, plus a refinement (e.g. Euler–Maclaurin) to obtain the $\tfrac12\log n$ correction and the constant $\sqrt{2\pi}$. Another route uses $\Gamma(n+1)=\int_0^\infty t^n e^{-t}\,dt$ and applies a Laplace/saddle-point argument (see {{< knowl id="saddle-point-lemma" text="saddle-point asymptotics" >}}).

In statistical mechanics, Stirling’s formula converts factorial growth in state counting (e.g. indistinguishable particles, multinomial occupations) into extensive terms of order $n$ plus subextensive corrections. This is one mechanism by which entropy densities emerge from microscopic counting.
