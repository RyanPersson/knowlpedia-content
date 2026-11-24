+++
id = "analytic-number-theory/centered-prime-sum"
title = "Centered prime-power ramp sum"
kind = "definition"
summary = "A weighted prime-power sum with the main term at s = 1 removed."
aliases = ["regularised prime sum", "regularized prime sum", "centered ramp sum"]
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/weighted-prime-sum", "analytic-number-theory/l-logarithmic-derivative-at-one"]
+++

A **centered prime-power ramp sum** removes an explicit main term from a [[analytic-number-theory/weighted-prime-sum|weighted prime sum]] with weight \(x/n-1\) for \(n\le x\). For the [[analytic-number-theory/riemann-zeta-function|Riemann zeta function]] and real \(x\ge1\), one normalization is
\[
G(x)=\sum_{n\le x}\Lambda(n)(x/n-1)-x\log x+(1+\gamma)x.
\]
Here \(\Lambda\) is the [[analytic-number-theory/von-mangoldt-function|von Mangoldt function]], and \(\gamma=\lim_{m\to\infty}(\sum_{j=1}^m1/j-\log m)\) is Euler’s constant. The centering subtracts \(x\log x-(1+\gamma)x\) from a finite sum.

## Twisting by a character

For a nonprincipal primitive [[analytic-number-theory/dirichlet-character|Dirichlet character]] \(\chi\), the corresponding normalization is
\[
G(\chi,x)=\sum_{n\le x}\Lambda(n)\chi(n)(x/n-1)+x\,\frac{L'(1,\chi)}{L(1,\chi)}.
\]
The [[analytic-number-theory/l-logarithmic-derivative-at-one|logarithmic derivative at one]] specifies the linear correction. If \(\chi\) is complex-valued, \(G(\chi,x)\) can also be complex-valued.

## References

- Manvir Jaswal, [§3.1, equations (3.1)–(3.2), the two ramp sums](https://manvirjaswal.github.io/papers/rh-dirichlet-after-alpoge/jaswal-rh-dirichlet-after-alpoge.pdf).
