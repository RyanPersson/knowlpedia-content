+++
id = "analytic-number-theory/windowed-landau-criterion"
title = "Windowed Landau criterion for Dirichlet zeros"
kind = "statement"
summary = "One-sided bounds on whole, arbitrarily late power windows exclude zeros to the right of the bound’s exponent."
aliases = ["windowed Landau theorem", "Landau on windows"]
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/centered-prime-sum", "analytic-number-theory/scale-window", "analytic-number-theory/dirichlet-character", "analytic-number-theory/dirichlet-l-function"]
+++

Fix a primitive [[analytic-number-theory/dirichlet-character|Dirichlet character]] \(\psi\). Let \(H=\langle\psi\rangle\) be its group of powers, and write \(\chi^*\) for the primitive character inducing \(\chi\). Using the zeta and character [[analytic-number-theory/centered-prime-sum|centered ramp sums]], form the real function
\[
G_\psi(x)=G(x)+\frac{1}{3|H|+1}
       \sum_{\substack{\chi\in H\\\chi\ne 1}}\operatorname{Re}G(\chi^*,x).
\]
The **windowed Landau criterion** states that if, for fixed \(0<\theta<1\) and \(\lambda>1\), the bound \(G_\psi(x)\le x^\theta\) holds for every real \(x\) in arbitrarily late [[analytic-number-theory/scale-window|power windows]] \([Y,Y^\lambda]\), then every [[analytic-number-theory/dirichlet-l-function|\(L(s,\chi^*)\)]] with \(\chi\in H\) is free of zeros in \(\operatorname{Re}s>\theta\).

## A single character family

For the primitive nonprincipal character of modulus \(4\), \(H\) has order two. The function to bound is \(G(x)+\tfrac17\operatorname{Re}G(\psi,x)\). The conclusion covers both the [[analytic-number-theory/riemann-zeta-function|zeta function]] and \(L(s,\psi)\). If the hypothesis holds for exponents arbitrarily close to \(1/2\) from above, any zero to the right of \(1/2\) would violate one of those conclusions.

## References

- Manvir Jaswal, [§§3.2–3.3, equation (3.3) and Theorem 3.2](https://manvirjaswal.github.io/papers/rh-dirichlet-after-alpoge/jaswal-rh-dirichlet-after-alpoge.pdf).
- Siniša Slijepčević, [§2, Proposition 2.2](https://hexagonmath.org/pdf/2611.00812).
