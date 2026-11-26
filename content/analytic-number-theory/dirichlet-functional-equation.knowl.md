+++
id = "analytic-number-theory/dirichlet-functional-equation"
title = "Functional equation of a primitive Dirichlet L-function"
kind = "theorem"
summary = "The completed L-function at s equals the conjugate character’s completed L-function at 1−s up to a constant of absolute value one."
domains = ["analytic-number-theory"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/dirichlet-l-function", "real-analysis/gamma-function"]
+++

Let \(\chi\) be a [[analytic-number-theory/primitive-dirichlet-character|primitive Dirichlet character]] of [[analytic-number-theory/dirichlet-conductor|conductor]] \(q\), and let \(a\) be \(0\) or \(1\) according as \(\chi(-1)=1\) or \(-1\). The completed [[analytic-number-theory/dirichlet-l-function|\(L\)-function]] \(\Lambda(s,\chi)=(q/\pi)^{(s+a)/2}\Gamma((s+a)/2)L(s,\chi)\) satisfies
\[
\Lambda(s,\chi)=\epsilon_\chi\Lambda(1-s,\bar\chi),\qquad |\epsilon_\chi|=1.
\]
The identity holds by meromorphic continuation. The [[real-analysis/gamma-function|gamma factor]] is finite and nonzero in \(0<\operatorname{Re}s<1\).

## Reflection of a zero

A zero in the open strip gives a zero of the inverse character at \(1-s\). An imprimitive character differs from its primitive representative by finitely many [[langlands/euler-product-and-local-factor|Euler factors]]. These do not vanish for \(\operatorname{Re}s>0\), so reflection transfers to zeros in that strip.

## References

- [NIST DLMF, §25.15(i), functional equation](https://dlmf.nist.gov/25.15)
