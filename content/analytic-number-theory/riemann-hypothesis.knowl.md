+++
id = "analytic-number-theory/riemann-hypothesis"
title = "Riemann hypothesis"
kind = "statement"
summary = "Every nontrivial zero of the Riemann zeta function has real part one half."
aliases = ["RH", "Riemann Hypothesis"]
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/riemann-zeta-function"]
+++

The **Riemann hypothesis** (RH) states that each zero \(\rho\) of the [[analytic-number-theory/riemann-zeta-function|Riemann zeta function]] in \(0<\operatorname{Re}\rho<1\) satisfies \(\operatorname{Re}\rho=\tfrac12\). This vertical line is the **critical line**.

## What this says about primes

Put \(\psi(x)=\sum_{n\le x}\Lambda(n)\), using the [[analytic-number-theory/von-mangoldt-function|von Mangoldt function]]. RH is equivalent to the estimate \(\psi(x)=x+O(\sqrt{x}\log^2 x)\) as \(x\to\infty\). The error measures how far the weighted count of prime powers deviates from \(x\). The [[analytic-number-theory/windowed-landau-criterion|estimate on windows]] in Chojecki’s post uses a different weight.

## References

- Enrico Bombieri, [Clay problem description, §I, the statement of RH](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf).
- Kiran Kedlaya, [Notes on analytic number theory, §7.3, the error estimate for the prime number theorem](https://kskedlaya.org/ant/part-2-4.html).
