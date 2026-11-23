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

A **centered prime-power ramp sum** subtracts the main term from a [[analytic-number-theory/weighted-prime-sum|weighted prime sum]] with weight \(x/n-1\) for \(n\le x\). For the zeta function the normalization used here is
\[
G(x)=\sum_{n\le x}\Lambda(n)(x/n-1)-x\log x+(1+\gamma)x,
\]
where \(\gamma\) is Euler’s constant. This is the meaning of “regularised” in the post. The input sum is already finite.

## The character term

For a nonprincipal primitive character \(\chi\), the corresponding expression is
\[
G(\chi,x)=\sum_{n\le x}\Lambda(n)\chi(n)(x/n-1)+x\,\frac{L'(1,\chi)}{L(1,\chi)}.
\]
The [[analytic-number-theory/l-logarithmic-derivative-at-one|logarithmic derivative]] supplies the correction. An upper bound applies to a real-valued combination of such sums.

## References

- Levent Alpöge, [announcement, p. 3, item 5](https://alpo.ge/remark.pdf).
- Manvir Jaswal, [§3.1, equations (3.1)–(3.2)](https://manvirjaswal.github.io/papers/rh-dirichlet-after-alpoge/jaswal-rh-dirichlet-after-alpoge.pdf).
