+++
id = "harmonic-analysis/theta-transformation-dirichlet-character"
title = "Theta transformation for a primitive Dirichlet character"
kind = "theorem"
summary = "Reciprocal Gaussian scales exchange a primitive character with its complex conjugate."
domains = ["harmonic-analysis"]
section_mode = "progressive"
prerequisites = ["analytic-number-theory/primitive-dirichlet-character","analytic-number-theory/dirichlet-character-parity","harmonic-analysis/dirichlet-theta-series","analytic-number-theory/dirichlet-gauss-sum","harmonic-analysis/poisson-summation-on-a-progression","functional-analysis/fourier-transform-schwartz-space","real-analysis/gaussian-integral"]
+++

Let \(\chi\) be a [[analytic-number-theory/primitive-dirichlet-character|primitive Dirichlet character]] of conductor \(q>1\) and [[analytic-number-theory/dirichlet-character-parity|parity]] \(a\). Its [[harmonic-analysis/dirichlet-theta-series|theta series]] and its [[analytic-number-theory/dirichlet-gauss-sum|Gauss sum]] satisfy, for \(t>0\),
\[
\theta_\chi(t)=\epsilon_\chi t^{-a-1/2}\theta_{\bar\chi}(1/t),\qquad
\epsilon_\chi=\frac{\tau(\chi)}{i^a\sqrt q},\qquad |\epsilon_\chi|=1 .
\]

## Proof

Apply [[harmonic-analysis/poisson-summation-on-a-progression|Poisson summation]] to \(f(x)=x^ae^{-\pi t x^2/q}\) on each residue class \(b\bmod q\). Multiply by \(\chi(b)\) and sum over \(b\). The finite sum at frequency \(m/q\) is \(\overline{\chi(m)}\tau(\chi)\) by the [[analytic-number-theory/dirichlet-gauss-sum|Gauss sum formula]].

For \(g(x)=e^{-\pi T x^2}\), \(T=t/q\), its [[functional-analysis/fourier-transform-schwartz-space|Fourier transform]] is \(T^{-1/2}e^{-\pi\xi^2/T}\). To see this, differentiate the integral in \(\xi\) and use \(g'=-2\pi T xg\) to integrate by parts. One obtains \(\widehat g'=-(2\pi\xi/T)\widehat g\), and the [[real-analysis/gaussian-integral|Gaussian integral]] gives \(\widehat g(0)=T^{-1/2}\). For the odd weight, \(\widehat{xg}=-\widehat g'/(2\pi i)=(\xi/iT)\widehat g\). Hence
\[
 q^{-1}\widehat f(m/q)=(i^a\sqrt q)^{-1}t^{-a-1/2}m^a e^{-\pi m^2/(qt)}.
\]
Both sums over all integers are twice their positive halves, since parity makes each summand even and \(\chi(0)=0\) for \(q>1\). Dividing by two gives the identity. The Gauss sum norm gives \(|\epsilon_\chi|=1\).

## The constant character of modulus one

For \(\theta(t)=\sum_{n\ge1}e^{-\pi n^2t}\), the zero term contributes one to the two-sided sum. The same Poisson formula with \(q=1\), \(b=0\) and \(a=0\) gives \(1+2\theta(t)=t^{-1/2}(1+2\theta(1/t))\).

## References

- [Poisson summation by residue class](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean#L361)
- [Primitive Gauss sum and the inverse scale](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/Analytic/DirichletTheta.lean#L399)
