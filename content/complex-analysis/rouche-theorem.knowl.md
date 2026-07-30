+++
id = "complex-analysis/rouche-theorem"
title = "Rouché's theorem"
kind = "theorem"
summary = "A strict boundary perturbation does not change the number of zeros inside a contour."
aliases = ["Rouche theorem", "Rouché theorem"]
domains = ["complex-analysis"]
section_mode = "progressive"
+++

Let \(\gamma\) be a positively oriented simple closed contour, and suppose \(f\) and \(g\) are holomorphic on a domain containing \(\gamma\) and its interior. If
\[
|g(z)|<|f(z)|\qquad(z\in\gamma),
\]
then \(f\) and \(f+g\) have the same number of zeros inside \(\gamma\), counted with multiplicity.

## Argument-principle proof

For \(0\le t\le1\), the inequality ensures that \(f+tg\) never vanishes on \(\gamma\). Hence the winding number of \((f+tg)\circ\gamma\) about \(0\) is constant in \(t\). The [[complex-analysis/argument-principle|argument principle]] identifies that winding number with the number of interior zeros.

## Typical use

On \(|z|=R\), compare a polynomial with its dominant term. If the dominant term is strictly larger than the sum of the remaining terms, the theorem counts all roots inside the circle without locating them individually.

## Boundary warning

The strict inequality on the whole contour is essential to this formulation. Equality at a boundary point can allow a zero to cross the contour, changing the count.

## References

1. Lars V. Ahlfors, *Complex Analysis*, 3rd ed., McGraw–Hill, 1979. Relevant: Chapter 5, §2.
